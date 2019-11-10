from flask import Blueprint, request
from ..services.request_service import process_registration

# Initialize endpoint usage
user_api = Blueprint("user_api", __name__)

# Endpoint for user registration
@user_api.route("/register", methods=["POST"])
def register():
    # Get registration request body as json
    request_data = request.json

    # Process and validate registration request
    response_data = process_registration(request_data)

    # Return response with status code
    return response_data
