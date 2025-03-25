import pytest
from validate_user_data import validate_user_data

# Test valid input
def test_valid_user_data():
    user_data = {
        "username": "validUser123",
        "email": "user@example.com",
        "password": "Passw0rd!",
        "age": 25,
        "referral_code": "ABCDEFGH"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] == True
    assert result["errors"] == {}

# Test missing username
def test_missing_username():
    user_data = {
        "email": "user@example.com",
        "password": "Passw0rd!"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] == False
    assert "username" in result["errors"]

# Test invalid username format
def test_invalid_username_format():
    user_data = {
        "username": "invalid@name!",
        "email": "user@example.com",
        "password": "Passw0rd!"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] == False
    assert "username" in result["errors"]

# Test missing email
def test_missing_email():
    user_data = {
        "username": "validUser",
        "password": "Passw0rd!"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] == False
    assert "email" in result["errors"]

# Test invalid email format
def test_invalid_email():
    user_data = {
        "username": "validUser",
        "email": "invalid-email",
        "password": "Passw0rd!"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] == False
    assert "email" in result["errors"]

# Test missing password
def test_missing_password():
    user_data = {
        "username": "validUser",
        "email": "user@example.com"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] == False
    assert "password" in result["errors"]

# Test password without a number
def test_password_no_number():
    user_data = {
        "username": "validUser",
        "email": "user@example.com",
        "password": "Password!"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] == False
    assert "password" in result["errors"]

# Test password without a special character
def test_password_no_special_char():
    user_data = {
        "username": "validUser",
        "email": "user@example.com",
        "password": "Password1"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] == False
    assert "password" in result["errors"]

# Test invalid age (not a number)
def test_invalid_age_type():
    user_data = {
        "username": "validUser",
        "email": "user@example.com",
        "password": "Passw0rd!",
        "age": "twenty"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] == False
    assert "age" in result["errors"]

# Test age under 18
def test_underage():
    user_data = {
        "username": "validUser",
        "email": "user@example.com",
        "password": "Passw0rd!",
        "age": 17
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] == False
    assert "age" in result["errors"]

# Test invalid referral code
def test_invalid_referral_code():
    user_data = {
        "username": "validUser",
        "email": "user@example.com",
        "password": "Passw0rd!",
        "referral_code": "12345"
    }
    result = validate_user_data(user_data)
    assert result["is_valid"] == False
    assert "referral_code" in result["errors"]
