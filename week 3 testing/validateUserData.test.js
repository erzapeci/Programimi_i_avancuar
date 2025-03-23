const validateUserData = require('./validateUserData');

describe('validateUserData - Unit Tests', () => {
  // Test case for valid input
  describe('Valid Input', () => {
    test('should return valid when all required and optional fields are correctly filled', () => {
      const validData = {
        username: 'Valid_User123',
        email: 'valid@example.com',
        password: 'Password1!',
        age: 25,
        referralCode: 'ABCD1234'
      };
      const result = validateUserData(validData);
      expect(result.isValid).toBe(true);
      expect(result.errors).toEqual({});
    });
  });

  // Test case for invalid input with null or non-object data
  describe('Invalid Input - General Cases', () => {
    test('should fail when userData is null', () => {
      const result = validateUserData(null);
      expect(result.isValid).toBe(false);
      expect(result.errors.global).toBe('Invalid user data format');
    });

    test('should fail when userData is not an object', () => {
      const result = validateUserData('not_an_object');
      expect(result.isValid).toBe(false);
      expect(result.errors.global).toBe('Invalid user data format');
    });
  });

  // Test case for username validation
  describe('Username Validation', () => {
    test.each([
      [{ email: 'test@example.com', password: 'Password1!' }, 'Username is required'],
      [{ username: 'ab', email: 'test@example.com', password: 'Password1!' }, 'Username must be between 3 and 20 characters'],
      [{ username: 'abcdefghijklmnopqrstu', email: 'test@example.com', password: 'Password1!' }, 'Username must be between 3 and 20 characters'],
      [{ username: 'invalid@user!', email: 'test@example.com', password: 'Password1!' }, 'Username can only contain letters, numbers, and underscores']
    ])('should fail for username %o with error %s', (invalidData, expectedError) => {
      const result = validateUserData(invalidData);
      expect(result.isValid).toBe(false);
      expect(result.errors.username).toBe(expectedError);
    });
  });

  // Test case for email validation
  describe('Email Validation', () => {
    test('should fail when email is missing', () => {
      const invalidData = { username: 'ValidUser123', password: 'Password1!' };
      const result = validateUserData(invalidData);
      expect(result.isValid).toBe(false);
      expect(result.errors.email).toBe('Email is required');
    });

    test('should fail when email format is incorrect', () => {
      const invalidData = { username: 'ValidUser123', email: 'invalid@', password: 'Password1!' };
      const result = validateUserData(invalidData);
      expect(result.isValid).toBe(false);
      expect(result.errors.email).toBe('Invalid email format');
    });
  });

  // Test case for password validation
  describe('Password Validation', () => {
    test.each([
      [{ username: 'ValidUser123', email: 'test@example.com' }, 'Password is required'],
      [{ username: 'ValidUser123', email: 'test@example.com', password: 'Pa2!' }, 'Password must be at least 8 characters long'],
      [{ username: 'ValidUser123', email: 'test@example.com', password: 'Password!' }, 'Password must contain at least one number'],
      [{ username: 'ValidUser123', email: 'test@example.com', password: 'Password1' }, 'Password must contain at least one special character']
    ])('should fail for password %o with error %s', (invalidData, expectedError) => {
      const result = validateUserData(invalidData);
      expect(result.isValid).toBe(false);
      expect(result.errors.password).toBe(expectedError);
    });
  });

  // Test case for age validation (optional)
  describe('Age Validation (Optional)', () => {
    test.each([
      [{ username: 'ValidUser123', email: 'test@example.com', password: 'Password1!', age: 'eighteen' }, 'Age must be a number'],
      [{ username: 'ValidUser123', email: 'test@example.com', password: 'Password1!', age: 17 }, 'User must be at least 18 years old']
    ])('should fail for age %o with error %s', (invalidData, expectedError) => {
      const result = validateUserData(invalidData);
      expect(result.isValid).toBe(false);
      expect(result.errors.age).toBe(expectedError);
    });
  });

  // Test case for referral code validation (optional)
  describe('Referral Code Validation (Optional)', () => {
    test.each([
      [{ username: 'ValidUser123', email: 'test@example.com', password: 'Password1!', referralCode: 12345678 }, 'Referral code must be a string'],
      [{ username: 'ValidUser123', email: 'test@example.com', password: 'Password1!', referralCode: 'ABCD' }, 'Referral code must be exactly 8 characters']
    ])('should fail for referralCode %o with error %s', (invalidData, expectedError) => {
      const result = validateUserData(invalidData);
      expect(result.isValid).toBe(false);
      expect(result.errors.referralCode).toBe(expectedError);
    });
  });
});
