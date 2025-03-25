import re

def validate_user_data(user_data):
    """
    Validates user registration data
    
    Args:
        user_data (dict): The user data to validate with the following keys:
            - username (str): Required, 3-20 chars, alphanumeric
            - email (str): Required, valid format
            - password (str): Required, min 8 chars, at least 1 number and 1 special char
            - age (int, optional): The user's age, must be 18+ if provided
            - referral_code (str, optional): Must be exactly 8 chars if provided
            
    Returns:
        dict: Object with is_valid flag and any error messages
    """
    result = {
        "is_valid": True,
        "errors": {}
    }

    # Allowed fields
    allowed_fields = {"username", "email", "password", "age", "referral_code"}
    provided_fields = set(user_data.keys())

    # Check for extra fields
    extra_fields = provided_fields - allowed_fields
    if extra_fields:
        result["is_valid"] = False
        result["errors"]["extra_fields"] = f"Unexpected fields provided: {', '.join(extra_fields)}"

    # Check if user_data exists and is a dictionary
    if not user_data or not isinstance(user_data, dict):
        result["is_valid"] = False
        result["errors"]["global"] = ["Invalid user data format"]
        return result

    # Validate username
    if "username" not in user_data or not user_data["username"]:
        result["is_valid"] = False
        result["errors"].setdefault("username", []).append("Username is required")
    else:
        if not (3 <= len(user_data["username"]) <= 20):
            result["is_valid"] = False
            result["errors"].setdefault("username", []).append("Username must be between 3 and 20 characters")
        if not re.match(r'^[a-zA-Z0-9_]+$', user_data["username"]):
            result["is_valid"] = False
            result["errors"].setdefault("username", []).append("Username can only contain letters, numbers, and underscores")

    # Validate email
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if "email" not in user_data or not user_data["email"]:
        result["is_valid"] = False
        result["errors"].setdefault("email", []).append("Email is required")
    elif not re.match(email_regex, user_data["email"]):
        result["is_valid"] = False
        result["errors"].setdefault("email", []).append("Invalid email format")

    # Validate password
    if "password" not in user_data or not user_data["password"]:
        result["is_valid"] = False
        result["errors"].setdefault("password", []).append("Password is required")
    else:
        if len(user_data["password"]) < 8:
            result["is_valid"] = False
            result["errors"].setdefault("password", []).append("Password must be at least 8 characters long")
        if not re.search(r'\d', user_data["password"]):
            result["is_valid"] = False
            result["errors"].setdefault("password", []).append("Password must contain at least one number")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', user_data["password"]):
            result["is_valid"] = False
            result["errors"].setdefault("password", []).append("Password must contain at least one special character")

    # Validate age (optional)
    if "age" in user_data:
        if not isinstance(user_data["age"], int):
            result["is_valid"] = False
            result["errors"].setdefault("age", []).append("Age must be a number")
        elif user_data["age"] < 18:
            result["is_valid"] = False
            result["errors"].setdefault("age", []).append("User must be at least 18 years old")

    # Validate referral code (optional)
    if "referral_code" in user_data:
        if not isinstance(user_data["referral_code"], str):
            result["is_valid"] = False
            result["errors"].setdefault("referral_code", []).append("Referral code must be a string")
        elif len(user_data["referral_code"]) != 8:
            result["is_valid"] = False
            result["errors"].setdefault("referral_code", []).append("Referral code must be exactly 8 characters")

    return result
