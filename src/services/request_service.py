from ..schemas import request_schema
from .security_service import process_password
from marshmallow import ValidationError
from flask import make_response


# Checks if the key exists in the serialized request
def check_key_exists(key, request):
    return bool(key in request.keys())


# Process registration request data
def process_registration(request):
    try:
        # Validate registration data and proceed if successful
        # Throws ValidationError if and exception was thrown while validation
        request_schema.RegistrationSchema(strict=True).load(request)

        # No errors since validation was successful
        errors = []
        # Set the request status to successful
        status = "success"

    except ValidationError as validation_error:
        # Get the list of errors
        errors = validation_error.messages
        # Set request status to failed
        status = "failed"

    # Get number of online breaches for the user's password
    # Will be used on the frontend to double-check if the user still wants to use the password (if breaches were found)
    breaches = process_password(request["password"]) if check_key_exists("password", request) else None
        
    # Results of processing the the registration request
    response_data = {
        "type": "register user",
        "status": status,
        "errors": errors,
        "password_breaches": breaches
    }

    # Set status code depending on status of response
    status_code = 200 if response_data["status"] == "success" else 400

    # Return formatted response
    return make_response(response_data, status_code)
