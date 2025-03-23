/**
 * Checks the validity of user registration details
 * @param {Object} userData - The provided user information
 * @param {string} userData.username - Required: Username (3-20 characters, alphanumeric, underscores allowed)
 * @param {string} userData.email - Required: A properly formatted email address
 * @param {string} userData.password - Required: Minimum 8 characters, at least 1 number and 1 special character
 * @param {number} [userData.age] - Optional: Age (must be at least 18 if specified)
 * @param {string} [userData.referralCode] - Optional: Referral code (must be exactly 8 characters if provided)
 * @returns {Object} - Returns an object containing isValid status and any error messages
 */
function validateUserData(userData) {
    const validation = {
        isValid: true,
        errors: {}
    };

    // Ensure userData exists and is an object
    if (!userData || typeof userData !== 'object') {
        validation.isValid = false;
        validation.errors.global = "Invalid user data format";
        return validation;
    }

    // Username validation
    if (!userData.username) {
        validation.isValid = false;
        validation.errors.username = "Username is required";
    } else if (userData.username.length < 3 || userData.username.length > 20) {
        validation.isValid = false;
        validation.errors.username = "Username must be between 3 and 20 characters";
    } else if (!/^[a-zA-Z0-9_]+$/.test(userData.username)) {
        validation.isValid = false;
        validation.errors.username = "Username can only contain letters, numbers, and underscores";
    }

    // Email validation
    if (!userData.email) {
        validation.isValid = false;
        validation.errors.email = "Email is required";
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(userData.email)) {
        validation.isValid = false;
        validation.errors.email = "Invalid email format";
    }

    // Password validation
    if (!userData.password) {
        validation.isValid = false;
        validation.errors.password = "Password is required";
    } else if (userData.password.length < 8) {
        validation.isValid = false;
        validation.errors.password = "Password must be at least 8 characters long";
    } else if (!/\d/.test(userData.password)) {
        validation.isValid = false;
        validation.errors.password = "Password must contain at least one numeric digit";
    } else if (!/[!@#$%^&*(),.?":{}|<>]/.test(userData.password)) {
        validation.isValid = false;
        validation.errors.password = "Password must include at least one special character";
    }

    // Age validation (if provided)
    if (userData.age !== undefined) {
        if (typeof userData.age !== 'number') {
            validation.isValid = false;
            validation.errors.age = "Age must be a numeric value";
        } else if (userData.age < 18) {
            validation.isValid = false;
            validation.errors.age = "User must be at least 18 years old";
        }
    }

    // Referral code validation (if provided)
    if (userData.referralCode !== undefined) {
        if (typeof userData.referralCode !== 'string') {
            validation.isValid = false;
            validation.errors.referralCode = "Referral code must be a string";
        } else if (userData.referralCode.length !== 8) {
            validation.isValid = false;
            validation.errors.referralCode = "Referral code must be exactly 8 characters long";
        }
    }

    return validation;
}

module.exports = validateUserData;
