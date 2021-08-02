from werkzeug.exceptions import HTTPException


class SchemaValidationError(HTTPException):
    pass


class UsernameAlreadyExists(HTTPException):
    pass


class EmailAlreadyExists(HTTPException):
    pass


class PasswordTooShort(HTTPException):
    pass


class InvalidCredentials(HTTPException):
    pass


class InvalidUsernameOrPassword(HTTPException):
    pass


errors = {
    "UsernameAlreadyExists": {
        "message": "User with the given username already exists",
        "status": 400
        },

    "EmailAlreadyExists": {
        "message": "User with the given email already exists",
        "status": 400
        },

    "PasswordTooShort": {
        "message": "Password must be at least 8 characters long",
        "status": 400
        }
    
}