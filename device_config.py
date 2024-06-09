# simple script for RUTOS device provisioning
# change password, get device info, upgrade firmware, upload backup, apply backup

import argparse
from rutos_api.api import api
from rutos_api.logs import create_logger
from rutos_api.utils import DotDict
import yaml
import json

logger = create_logger(__name__)

def main():
    parser = argparse.ArgumentParser(description='Script for RUTOS device provisioning.')
    parser.add_argument('-i', '--device-ip', default='192.168.1.1' , help='Device IP address')
    parser.add_argument('-p', '--password', required=True, help='Password (default) for the configurable device')
    parser.add_argument('-u', '--username', required=False, help='Username for the configurable device')
    parser.add_argument('-n', '--new-password', required=False, help='New password for the configurable device')

    args = parser.parse_args()

    password = args.password
    username = args.username or 'admin'
    new_password = args.new_password
    device_ip = args.device_ip

    device = api(device_ip, password=password)
    logger.info(f'Device {device_ip}:')
    device.wait_until_alive()
    if new_password is not None:
        device.change_password(new_password)

    if data := device.request('system/device/status'):
        data = DotDict(data.json())
        if 'success' in data and data.success:
            data = data.data
            logger.info(f'{data.static.model} ({data.static.device_name}) SN: {data.mnfinfo.serial}')
    # data = device.get_bulk_config(['sim_switch', 'interfaces'])
    # data = yaml.dump(data, default_flow_style=False)
    # data = json.dumps(data, indent=4)
    # print(data)

    device.upgrade_firmware('user_data\\RUT9M_R_00.07.07.1_WEBUI.bin')
    device.wait_until_alive()

    device.upload_apply_backup('user_data\\base_config.tar.gz')
    device.wait_until_alive()

    data = device.get_bulk_config(['interfaces', 'ports_settings', 'port_based_vlan', 'openvpn'])
    data = yaml.dump(data, default_flow_style=False)
    # data = json.dumps(data, indent=4)
    print(data)


if __name__ == "__main__":
    main()