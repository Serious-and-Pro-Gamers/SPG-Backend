from ..app import ma
from marshmallow import fields, validate, validates, ValidationError
import re


# Registration schema for request field data
class RegistrationSchema(ma.Schema):
    # Set username as a required field and validate for character length
    username = fields.String(required=True, validate=validate.Length(min=5, max=12))
    # Set password as a required field and validate for character length
    password = fields.String(required=True, validate=validate.Length(min=8, max=20))

    # Further validate the password field
    @validates("password")
    def validate_password(self, password):
        # Regex patterns to check for at least one uppercase, lowercase, special char, and digit
        upper_pattern = re.compile(r"(?=.*[A-Z])")   
        lower_pattern = re.compile(r"(?=.*[a-z])")            
        special_pattern = re.compile(r"(?=.*[!@#\$%\^&\*])")
        digit_pattern = re.compile(r"(?=.*[0-9])")

        # Check the password for the regex patterns individually
        upper_search = re.search(upper_pattern, password)
        lower_search = re.search(lower_pattern, password)
        special_search = re.search(special_pattern, password)
        digit_search = re.search(digit_pattern, password)

        # Check if any of the regex patterns were not matched
        # Append any errors as a message to the errors list
        errors = []
        if not upper_search: 
            errors.append("Must have at least 1 uppercase letters [A-Z]")
        if not lower_search:
            errors.append("Must have at least 1 lowercase letters [a-z]")
        if not special_search:
            errors.append("Must have at least 1 special character [!@#$%^&*]")
        if not digit_search:
            errors.append("Must have at least 1 digit [0-9]")

        # If there is anything in the errors list, raise a ValidationErorr exception
        if errors:
            raise ValidationError(errors)
