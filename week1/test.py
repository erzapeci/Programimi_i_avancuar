# Import the datetime module to work with date and time
import datetime


def get_user_name():
    """
    Prompt the user to enter their name.
    Includes input validation to ensure the name is not left empty.
    
    Returns:
        str: The user's name if valid.
    """
    while True:  # Loop continuously until a valid name is provided
        try:
            # Ask the user to input their name and strip any extra spaces
            name = input("Please enter your name: ").strip()

            # If the input is empty, raise an exception to force re-entry
            if not name:
                raise ValueError("Name cannot be empty")

            # Return the valid name
            return name

        # Catch the ValueError and display the error message to the user
        except ValueError as e:
            print(e)


def main():
    """
    Main function to greet the user and display the current date and time.
    """
    # Display an initial greeting message
    print("Hello, World!")

    # Call the get_user_name function to retrieve a valid user name
    user_name = get_user_name()

    # Display a personalized greeting using the user's name
    print(f"Hello, {user_name}!")

    # Get the current date and time using datetime.now()
    current_time = datetime.datetime.now()

    # Format and display the current date and time nicely
    print("Current date and time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))


# Ensure the script only runs when executed directly, not when imported
if __name__ == "__main__":
    main()
