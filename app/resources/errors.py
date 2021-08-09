from werkzeug.exceptions import HTTPException

# class SchemaValidationError(HTTPException):
#     pass

class UpdateError(HTTPException):
    pass

class MissingRequiredArgument(HTTPException):
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

class NegativePrice(HTTPException):
    pass


class ServerError(HTTPException):
    pass


# We can use (response=Response(message, status=)) to have dinamic error messages

errors = {
    "UpdateError": {
        "message": "Invalid fields for update"
    },

    "MissingRequiredArguments": {
        "message": "Missing required arguments",
        "status": 400
    },

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
    },

    "InvalidCredentials": {
        "message": "Invalid credentials",
        "status": 400
    },

    "InvalidUsernameOrPassword": {
        "message": "Invalid username or password",
        "status": 400
    },

    "NegativePrice": {
        "message": "Price must be positive",
        "status": 400
    },

    "ServerError": {
        "message": "Unexpected error",
        "status": 500
    }  
    
}
