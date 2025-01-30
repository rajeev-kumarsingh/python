# Python Datetime

- Python's datetime module provides classes for manipulating dates and times.
- It includes functionalities like getting the current time, formatting dates, handling time zones, and performing date arithmetic.

#

# 🔹 Importing datetime

```
import datetime

```

# 📌 Getting Current Date & Time

```
from datetime import datetime

now = datetime.now()
print(now)  # 2025-01-30 12:34:56.789012

```

## Getting Specific Components

```
print(now.year)   # 2025
print(now.month)  # 1
print(now.day)    # 30
print(now.hour)   # 12
print(now.minute) # 34
print(now.second) # 56

```

## 📌 Creating a Specific DateTime

```
dt = datetime(2024, 12, 5, 15, 30, 45)
print(dt)  # 2024-12-05 15:30:45

```

## 📌 Formatting Dates (strftime)

```
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date)  # 2025-01-30 12:34:56

```

## 📌 Common Format Codes:

- %Y → Year (2025)
- %m → Month (01)
- %d → Day (30)
- %H → Hour (24-hour format)
- %I → Hour (12-hour format)
- %M → Minute
- %S → Second
- %A → Full weekday name (Thursday)
- %B → Full month name (January)

## 📌 Parsing Strings into Dates (strptime)

```
date_str = "2024-12-05 15:30:45"
dt_obj = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print(dt_obj)  # 2024-12-05 15:30:45

```

# 📌 Date Arithmetic (Adding/Subtracting Days)

```
from datetime import timedelta

tomorrow = now + timedelta(days=1)
yesterday = now - timedelta(days=1)

print(tomorrow)  # 2025-01-31 12:34:56
print(yesterday) # 2025-01-29 12:34:56

```

## 📌 Getting Time Difference

```
dt1 = datetime(2025, 1, 30, 12, 0, 0)
dt2 = datetime(2025, 1, 25, 12, 0, 0)

diff = dt1 - dt2
print(diff.days)   # 5
print(diff.total_seconds())  # 432000.0

```

## 📌 Working with Time Zones (pytz)

Python's datetime by default is timezone-naive. To work with time zones, use the pytz library.

```
pip install pytz

```

### Converting Time Zones

```
import pytz

utc_now = datetime.now(pytz.utc)
india_time = utc_now.astimezone(pytz.timezone("Asia/Kolkata"))

print(india_time)  # 2025-01-30 18:04:56+05:30

```

## 📌 Getting Timestamps (Epoch Time)

```
timestamp = now.timestamp()
print(timestamp)  # 1738239296.789012 (Seconds since Jan 1, 1970)

dt_from_timestamp = datetime.fromtimestamp(timestamp)
print(dt_from_timestamp)  # 2025-01-30 12:34:56

```

## 📌 Comparing Dates

```
dt1 = datetime(2025, 1, 30, 12, 0, 0)
dt2 = datetime(2025, 1, 31, 12, 0, 0)

print(dt1 < dt2)  # True
print(dt1 == dt2) # False

```
