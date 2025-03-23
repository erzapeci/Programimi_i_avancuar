# Import the datetime module to work with date and time
import datetime

# Define a function to get the user's name with input validation
def get_user_name():
    """
    This function repeatedly prompts the user to enter their name.
    It ensures that the input is not left empty.
    Returns:
        str: A valid, non-empty string representing the user's name.
    """
    while True:
        try:
            # Prompt the user for their name and remove any leading/trailing spaces
            name = input("Please enter your name: ").strip()
            
            # Check if the user entered a non-empty name
            if not name:
                # Raise an error if the input is empty
                raise ValueError("Name cannot be empty")
            
            # Return the valid name if no errors occurred
            return name

        # Handle the ValueError and display the error message to the user
        except ValueError as e:
            print(e)

# Define the main function to run the program
def main():
    """
    The main function that orchestrates the greeting program.
    It prints a greeting, asks for the user's name, and displays the current date and time.
    """
    # Display a friendly initial greeting
    print("Hello, World!")
    
    # Call the get_user_name function to obtain a valid name from the user
    user_name = get_user_name()
    
    # Greet the user personally with their provided name
    print(f"Hello, {user_name}!")
    
    # Fetch the current date and time from the system
    current_time = datetime.datetime.now()
    
    # Display the current date and time in a readable format
    print("Current date and time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

# Ensure the script runs only when executed directly (not imported as a module)
if __name__ == "__main__":
    main()
