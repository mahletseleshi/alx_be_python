# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the current date and time as "YYYY-MM-DD HH:MM:SS"
    formatted_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the formatted current date and time
    print(f"Current date and time: {formatted_current_date}")
    
    # Return the current date for use in other functions
    return current_date

def calculate_future_date(current_date, days_to_add):
    # Calculate the future date by adding the specified number of days to the current date
    future_date = current_date + timedelta(days=days_to_add)
    
    # Format the future date as "YYYY-MM-DD"
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    
    # Print the formatted future date
    print(f"Future date: {formatted_future_date}")

def main():
    # Display the current date and time
    current_date = display_current_datetime()
    
    # Prompt the user to enter the number of days to add
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate and display the future date
    calculate_future_date(current_date, days_to_add)

if __name__ == "__main__":
    main()
