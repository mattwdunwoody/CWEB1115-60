# **YOU WILL NEED TO RUN "pip install requests" IN CONSOLE TO RUN!!!**

import datetime
import requests

# Function to find the day of the week for a given date
def find_day_of_week(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        day_index = date_obj.weekday()
        return days_of_week[day_index]
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# Function to calculate age based on birthdate
def calculate_age(birthdate):
    try:
        birthdate_obj = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
        today = datetime.datetime.now()
        age = today.year - birthdate_obj.year - ((today.month, today.day) < (birthdate_obj.month, birthdate_obj.day))
        return age
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."

# Function to generate a list of leap years in a given range
def list_leap_years(start_year, end_year):
    leap_years = [year for year in range(start_year, end_year + 1) if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)]
    return leap_years

# Function to calculate days until an upcoming holiday
def days_until_holiday(date_string, holiday_date):
    try:
        today = datetime.datetime.strptime(date_string, "%Y-%m-%d")
        holiday = datetime.datetime.strptime(holiday_date, "%Y-%m-%d")
        days_until = (holiday - today).days
        if days_until < 0:
            return "The holiday has already passed."
        return days_until
    except ValueError:
        return "Invalid date format. Please use YYYY-MM-DD."
    
def historical_events_of_date(date_string):
    api_url = "http://history.muffinlabs.com/date"
    try:
        _user_date = datetime.datetime.strptime(date_string, "%m-%d")
        try:
            response = requests.get(api_url, {'date': _user_date})
            response.raise_for_status()
            date_data= response.json()

            historical_events = date_data['data']['Events']
            return historical_events
        
        except requests.exceptions.HTTPError as http_error:
            print(f"HTTP Error: {http_error}")
        except requests.exceptions.ConnectionError as connection_error:
            print(f"Error Connecting: {connection_error}")
        except requests.exceptions.Timeout as timeout:
            print(f"Timeout Error: {timeout}")
        except requests.exceptions.RequestException as request_error:
            print(f"An error occurred: {request_error}")

    except ValueError:
        return "Invalid date format. Please use MM-DD."

# Example usage of the functions
if __name__ == "__main__":
    while True:
        print("Date Magic Menu:")
        print("1. Find the day of the week")
        print("2. Calculate age")
        print("3. Find leap years")
        print("4. Calculate days until a holiday")
        print("5. Exit")
        print("6. Extra credit: get historical events of date")
        choice = input("Enter your choice: ")

        if choice == "1":
            user_date = input("Enter a date (YYYY-MM-DD): ")
            print("Day of the week:", find_day_of_week(user_date))
        elif choice == "2":
            user_date = input("Enter your birthdate (YYYY-MM-DD): ")
            print("Your age:", calculate_age(user_date), "years")
        elif choice == "3":
            start_year = int(input("Enter the start year: "))
            end_year = int(input("Enter the end year: "))
            print("Leap years:", list_leap_years(start_year, end_year))
        elif choice == "4":
            user_date = input("Enter today's date (YYYY-MM-DD): ")
            holiday_date = input("Enter the holiday date (YYYY-MM-DD): ")
            print("Days until the holiday:", days_until_holiday(user_date, holiday_date))
        elif choice == "5":
            print("Exiting Date Magic. Goodbye!")
            break
        elif choice == "6":
            user_date = input("Enter a date (MM-DD): ")

            _events = historical_events_of_date(user_date)
            if(_events):
                print(f"\nHistorical events for {user_date}:\n")
                for event in _events:
                    print(f"{event['year']}: {event['text']}")
                input("Press Enter to continue...")
            else:
                print("No historical events found for the given date.")
        else:
            print("Invalid choice. Please select a valid option.")