from datetime import datetime

# Read the date and time values from the text file
with open('dates.txt', 'r') as file:
    lines = file.readlines()

# Assuming the file contains two lines: start date/time and end date/time
start_datetime_str = lines[0].strip()[:19]
end_datetime_str = lines[1].strip()[:19]


# Convert the text representations into datetime objects
start_datetime = datetime.strptime(start_datetime_str, '%Y-%m-%d %H:%M:%S')
end_datetime = datetime.strptime(end_datetime_str, '%Y-%m-%d %H:%M:%S')

# Calculate the time difference
time_difference = end_datetime - start_datetime

# Calculate time difference in seconds, minutes, and hours
seconds_difference = time_difference.total_seconds()
minutes_difference = seconds_difference / 60
hours_difference = minutes_difference / 60

# Print the results
print(f"Time difference in seconds: {seconds_difference} seconds")
print(f"Time difference in minutes: {minutes_difference} minutes")
print(f"Time difference in hours: {hours_difference} hours")
