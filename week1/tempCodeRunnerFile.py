# Import necessary module for date and time
import datetime

def get_user_name():
    """Prompt user for their name with input validation"""
    while True:
        try:
            name = input("Please enter your name: ").strip()
            if not name:
                raise ValueError("Name cannot be empty")
            return name
        except ValueError as e:
            print(e)

def main():
    # Print initial greeting
    print("Hello, World!")
    
    # Get user's name with error handling
    user_name = get_user_name()
    
    # Personalized greeting
    print(f"Hello, {user_name}!")
    
    # Get and display current date/time
    current_time = datetime.datetime.now()
    print("Current date and time:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

if __name__ == "__main__":
    main()