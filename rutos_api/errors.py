from enum import Enum

class ErrorCodes(Enum):
    UCI_CREATE_ERROR = 106
    INVALID_STRUCTURE = 107
    SECTION_CREATION_DENIED = 108
    NAME_ALREADY_USED = 109
    NAME_NOT_PROVIDED = 110
    DELETE_NOT_ALLOWED = 111
    CONFIG_DELETION_DENIED = 112
    INVALID_SECTION = 113
    NO_BODY_PROVIDED = 114
    UCI_SET_ERROR = 115
    INVALID_QUERY_PARAMETER = 116
    GENERAL_CONFIG_ERROR = 117
    UNAUTHORIZED = 120
    LOGIN_FAILED = 121
    GENERAL_STRUCTURE = 122
    JWT_TOKEN_INCORECT = 123
    NO_ENOUGH_SPACE = 150
    FILE_SIZE_LIMIT = 151
    UNKNOW_ERROR = -1

    def __str__(self):
        return ERROR_DESCRIPTIONS.get(self, "Unknown error")

ERROR_DESCRIPTIONS = {
    ErrorCodes.UCI_CREATE_ERROR : "UCI CREATE error",
    ErrorCodes.INVALID_STRUCTURE : "Invalid structure",
    ErrorCodes.SECTION_CREATION_DENIED : "Section creation is not allowed",
    ErrorCodes.NAME_ALREADY_USED : "Name already used",
    ErrorCodes.NAME_NOT_PROVIDED : "Name not provided",
    ErrorCodes.DELETE_NOT_ALLOWED : "DELETE not allowed",
    ErrorCodes.CONFIG_DELETION_DENIED : "Deletion of whole configuration is not allowed",
    ErrorCodes.INVALID_SECTION : "Invalid section provided",
    ErrorCodes.NO_BODY_PROVIDED : "No body provided for the request",
    ErrorCodes.UCI_SET_ERROR : "UCI SET error",
    ErrorCodes.INVALID_QUERY_PARAMETER : "Invalid query parameter",
    ErrorCodes.GENERAL_CONFIG_ERROR : "General configuration error",
    ErrorCodes.UNAUTHORIZED : "Unauthorized access",
    ErrorCodes.LOGIN_FAILED : "Login failed for any reason",
    ErrorCodes.GENERAL_STRUCTURE : "General structure of request is incorrect",
    ErrorCodes.JWT_TOKEN_INCORECT : "JWT token that is provided with authorization header is invalid - unparsable, incomplete, etc.",
    ErrorCodes.NO_ENOUGH_SPACE : "Not enough free space in the device (when uploading files)",
    ErrorCodes.FILE_SIZE_LIMIT : "File size is bigger than the maximum size allowed (when uploading files)",
    }

