from datetime import datetime

# datetime.today() = datetime.now(timezone) when timezone is undefined
now = datetime.now()

current_time = now.strftime("%Y-%m-%d %H:%M:%S")

print("Current date and time :\n" + current_time)
