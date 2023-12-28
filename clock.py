import datetime
import pytz

def display_world_clock(timezones):
    while True:
        current_time = datetime.datetime.utcnow()

        print("\nWorld Clock:")
        for timezone_name, offset in timezones.items():
            timezone = pytz.timezone(timezone_name)
            localized_time = current_time + datetime.timedelta(seconds=offset)
            formatted_time = localized_time.strftime("%Y-%m-%d %H:%M:%S")
            print(f"{timezone_name}: {formatted_time}")

        try:
            update_interval = int(input("\nEnter update interval in seconds (0 to exit): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if update_interval == 0:
            print("Exiting world clock.")
            break

        print("\nPress Enter to update or wait for the next interval...")
        user_input = input()
        if user_input.lower() == 'exit':
            print("Exiting world clock.")
            break

if __name__ == "__main__":
    # Define your desired timezones and their offsets in seconds
    # You can find a list of supported timezones at https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    timezones = {
        'America/New_York': -5 * 3600,  # Eastern Time
        'Europe/London': 0,             # Greenwich Mean Time
        'Asia/Tokyo': 9 * 3600,         # Japan Standard Time
    }

    print("Welcome to the Customizable World Clock!")
    display_world_clock(timezones)
