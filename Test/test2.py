import pytz

# Set the desired time zone
timezone = pytz.timezone('UTC')

# Use the time zone in your code
timestamp = item['time']
time_str = datetime.utcfromtimestamp(timestamp).replace(tzinfo=timezone).strftime('%Y-%m-%d %H:%M:%S')