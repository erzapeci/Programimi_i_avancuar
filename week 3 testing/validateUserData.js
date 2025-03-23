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
    // Initialize the result object with a default 'valid' state
    const validation = {
        isValid: true,
        errors: {}  // This will hold any validation errors per field
    };

    // Ensure userData exists and is an object
    if (!userData || typeof userData !== 'object') {
        validation.isValid = false;
        validation.errors.global = "Invalid user data format";
        return validation; // Stop early if data is missing or incorrectly formatted
    }

    /**
     * Username validation
     */
    if (!userData.username) {
        // Check if username is provided
        validation.isValid = false;
        validation.errors.username = "Username is required";
    } else if (userData.username.length < 3 || userData.username.length > 20) {
        // Check username length constraints
        validation.isValid = false;
        validation.errors.username = "Username must be between 3 and 20 characters";
    } else if (!/^[a-zA-Z0-9_]+$/.test(userData.username)) {
        // Ensure username contains only allowed characters
        validation.isValid = false;
        validation.errors.username = "Username can only contain letters, numbers, and underscores";
    }

    /**
     * Email validation
     */
    if (!userData.email) {
        // Email must be provided
        validation.isValid = false;
        validation.errors.email = "Email is required";
    } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(userData.email)) {
        // Check email format using regex
        validation.isValid = false;
        validation.errors.email = "Invalid email format";
    }

    /**
     * Password validation
     */
    if (!userData.password) {
        // Password is mandatory
        validation.isValid = false;
        validation.errors.password = "Password is required";
    } else if (userData.password.length < 8) {
        // Enforce minimum password length
        validation.isValid = false;
        validation.errors.password = "Password must be at least 8 characters long";
    } else if (!/\d/.test(userData.password)) {
        // Ensure password has at least one number
        validation.isValid = false;
        validation.errors.password = "Password must contain at least one numeric digit";
    } else if (!/[!@#$%^&*(),.?":{}|<>]/.test(userData.password)) {
        // Ensure password has at least one special character
        validation.isValid = false;
        validation.errors.password = "Password must include at least one special character";
    }

    /**
     * Age validation (optional field)
     */
    if (userData.age !== undefined) { // Only validate age if it's provided
        if (typeof userData.age !== 'number') {
            // Ensure age is a number
            validation.isValid = false;
            validation.errors.age = "Age must be a numeric value";
        } else if (userData.age < 18) {
            // Check the age requirement
            validation.isValid = false;
            validation.errors.age = "User must be at least 18 years old";
        }
    }

    /**
     * Referral code validation (optional field)
     */
    if (userData.referralCode !== undefined) { // Only validate if provided
        if (typeof userData.referralCode !== 'string') {
            // Referral code must be a string
            validation.isValid = false;
            validation.errors.referralCode = "Referral code must be a string";
        } else if (userData.referralCode.length !== 8) {
            // Referral code must be exactly 8 characters
            validation.isValid = false;
            validation.errors.referralCode = "Referral code must be exactly 8 characters long";
        }
    }

    // Return the final validation object containing the overall status and any errors
    return validation;
}

// Export the function for use in other files/modules
module.exports = validateUserData;
