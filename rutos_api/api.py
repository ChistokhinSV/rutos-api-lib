import requests
import time
from rutos_api.logs import create_logger
from rutos_api.errors import ErrorCodes
from rutos_api.utils import actions
import urllib3
from urllib3.exceptions import InsecureRequestWarning, ConnectTimeoutError
import yaml
from requests.adapters import HTTPAdapter
import os

# if token valid for less than TOKEN_REMAIN_TIMEOUT seconds - updsate token
TOKEN_REMAIN_TIMEOUT = 20

# default request timeout
DEFAULT_REQUEST_TIMEOUT = 10

logger = create_logger(__name__)
urllib3.disable_warnings(InsecureRequestWarning)

class api(object):
    def __init__(
        self, host: str, port: int = 443, username: str = "admin", password: str = ""
    ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.base_url = f'https://{host}{f":{port}" if port != 443 else ""}/api'
        self.token = None
        self.token_expire = None
        self.session = requests.Session()
        self.session.verify = False

    @property
    def url(self) -> str:
        return f'{self.base_url}'

    def get_error(self, response: requests.Response):
        errors = []
        if response is None:
            return "Empty data"
        if response.status_code >= 300 or response.status_code < 200:
            errors.append(f"Request Error: {response.status_code}")
        data = response.json()
        if "errors" in data:
            errors.extend(
                f'{error.get("source", "GENERAL")} {error.get("section", "(SECTION)")} {error["code"]}: {error["error"]}'
                for error in data["errors"]
            )
        return "\n".join(errors)

    def request(
        self,
        url: str,
        method: str = "GET",
        body: dict = None,
        headers: dict = None,
        timeout: int = DEFAULT_REQUEST_TIMEOUT,
        max_retries=3,
        auth=True,
        files=None,
    ) -> requests.Response | None:
        if body is None:
            body = {}
        if headers is None:
            headers = {}

        adapter = HTTPAdapter(max_retries=max_retries)
        self.session.mount("http://", adapter)
        self.session.mount("https://", adapter)

        if auth and ("username" not in body or "password" not in body):
            if (
                self.token is None
                or self.token_expire is None
                or self.token_expire - TOKEN_REMAIN_TIMEOUT < time.time()
            ):
                self.login()
            headers["Authorization"] = f"Bearer {self.token}"
        try:
            url = f'{self.base_url}/{url.lstrip("/")}'
            response = self.session.request(
                method=method,
                url=url,
                json=body,
                headers=headers,
                timeout=timeout,
                files=files,
            )
            logger.info(f"Request: {method} {url} {self.get_error(response)}")
            response.raise_for_status()
            # if unauthorized and bearer expired - try again
            if (
                response.status_code == 401
                and "errors" in response.json()
                and response.json()["errors"][0]["code"]
                == ErrorCodes.JWT_TOKEN_INCORECT
            ):
                self.login()
                response = self.session.request(
                    method=method,
                    url=url,
                    json=body,
                    headers=headers,
                    timeout=timeout,
                    files=files,
                )
                if response.status_code != 200:
                    logger.error(self.get_error(response))
                    exit(response.status_code)
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"Error: {e}")

    def login(self):
        credentials = {"username": self.username, "password": self.password}
        response = self.request(url="/login", method="POST", body=credentials)
        if response is None:
            self.token = None
            self.token_expire = None
            return None
        if response.status_code != 200:
            logger.error(self.get_error(response))
            exit(response.status_code)
        data = response.json()
        self.token = data["data"]["token"]
        self.token_expire = data["data"]["expires"] + time.time()
        return self.token

    def get_config(self, config: str, sid: str = "config", id="") -> dict | None:
        url = f"{config}/config/{id}"
        response = self.request(url=url)

        if response is not None and (
            response.status_code == 200 and "data" in response.json()
        ):
            return response.json()["data"]

    def get_bulk_config(self, configs: list) -> dict:
        result = {}
        body = {
            "data": [
                {"endpoint": f"/api/{config}/config", "method": "GET"}
                for config in configs
            ]
        }
        response = self.request(url="/bulk", method="POST", body=body)
        if (
            response is not None
            and response.status_code >= 200
            and response.status_code < 300
        ):
            result = dict(zip(configs, response.json()["data"]))
            for section, config in result.items():
                if "success" in config and config["success"] and "data" in config:
                    result[section] = config["data"]
                elif "errors" in config:
                    result[section] = "\n".join([
                        f'# {error["source"]} {error["code"]}: {error["error"]}'
                        for error in config["errors"]
                    ])
                else:
                    result[section] = "# Unknown error"
        return result

    def data_if_valid(self, response: requests.Response):
        if (
            response is not None
            and response.status_code >= 200
            and response.status_code < 300
        ):
            return response.json()["data"] if "data" in response.json() else response.json()
        logger.error(self.get_error(response))

    def update_config(
        self, config, sid="config", id="", data=None, files=None, method="POST"
    ) -> dict | None:
        if data is None:
            data = {}
        url = f"{config}/{sid}/{id}"
        response = self.request(url=url, method=method, body=data, files=files)
        return self.data_if_valid(response)

    def update_config_with_file(
        self, config, sid="config", id="", data=None, filename=None
    ):
        if filename is None:
            raise ValueError("filename is not defined")
        with open(filename, "rb") as file:
            files = {
                "file": (os.path.basename(filename), file, "application/octet-stream")
            }
            return self.update_config(config, sid=sid, id=id, data=data, files=files)

    def upload_backup(self, filename: str):
        data = {
            "encrypt": "0",
            "password": "",
        }
        return self.perform_action_with_file("backup", "upload", filename, data=data)

    def upload_apply_backup(self, filename: str):
        data = {
            # TODO implement encrypted backups upload
            "encrypt": "0",
            "password": "",
        }
        upload = self.perform_action_with_file("backup", "upload", filename, data=data)
        logger.info(f"Uploaded backup on {self.host}:{self.port} ({filename}) : {upload}")
        logger.info(f"Applying backup on {self.host}:{self.port} ({filename})...")
        data = {
            "data": {
                "encrypt": "0",
                "password": ""
            }
        }
        result = self.perform_action("backup", "apply", data=data)
        logger.info(f"Applied backup on {self.host}:{self.port} ({filename}) : {result}")
        return result

    def perform_action(self, config: str, action: str, files=None, data=None, timeout = DEFAULT_REQUEST_TIMEOUT):
        if data is None:
            data = {}
        url = f"{config}/actions/{action}"

        response = self.request(url=url, method="POST", body=data, files=files, timeout=timeout)
        return self.data_if_valid(response)

    def perform_action_with_file(
        self, config: str, action: str, filename=None, data=None, timeout = 60*2
    ):
        if filename is None:
            raise ValueError("filename is not defined")
        with open(filename, "rb") as file:
            files = {
                "file": (os.path.basename(filename), file, "application/octet-stream")
            }
            return self.perform_action(config, action, files=files, data=data, timeout=timeout)

    def upgrade_firmware(self, filename: str):
        data = {
            "force_upgrade": "1",
            "keep_settings": "1",
        }
        logger.info(f"Upgrading firmware on {self.host}:{self.port} ({filename})...")
        result = self.perform_action_with_file(
            "firmware", "upload_device_firmware", filename, data=data
        )
        logger.info(f"{self.host}:{self.port} uploaded: {result}")
        data = {
            "data": {
                "keep_settings": "1"
            }
        }
        result = self.perform_action('firmware', 'upgrade', data=data, timeout=60*3)
        logger.info(f"{self.host}:{self.port} upgraded: {result}")
        return result

    def is_alive(self):
        urllib3.disable_warnings(ConnectTimeoutError)
        response = self.request(
            url="unauthorized/status", timeout=1, max_retries=0, auth=False
        )
        urllib3.simplefilter("default", urllib3.exceptions.ConnectTimeoutError)
        return response is not None

    def wait_until_alive(self, retry_interval=10, retries=30):
        for _ in range(retries):
            logger.info(f"Waiting for {self.host}:{self.port} to be alive...")
            if self.is_alive():
                return
            time.sleep(retry_interval)
        logger.error(f"Can't connect to {self.host}:{self.port}")
        exit(ErrorCodes.UNKNOW_ERROR)

    def change_password(self, new_password: str, old_password: str = None, username: str = None):
        if username is None:
            username = self.username

        if old_password is None:
            old_password = self.password

        users = self.get_config("users")
        if users is None:
            logger.error(f"Can't change password for {username}")
            return None

        user_id = None
        for user in users:
            if user["username"] == username:
                user_id = user["id"]
                break

        if user_id is None:
            logger.error(f"Can't find user id for {username}")
            return None

        data = {
            "data": {
                "current_password": old_password,
                "password": new_password,
                "password_confirm": new_password,
            }
        }
        response = self.update_config("users", id = str(user_id), data=data, method="PUT")
        if response is not None:
            self.password = new_password
        return response
