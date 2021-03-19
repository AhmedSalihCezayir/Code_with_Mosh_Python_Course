import time
from datetime import datetime, timedelta


def send_emails():
    for _ in range(100000):
        pass


start = time.time()
send_emails()
end = time.time()
duration = end - start
print("duration:", duration)

# --------------------------------------------------------

dt1 = datetime(2021, 2, 7)
dt2 = datetime.now()

# This method turns strings to a datetime objects
dt = datetime.strptime("2018/01/01", "%Y/%m/%d")
dt = datetime.fromtimestamp(time.time())
print(dt)
print(f"{dt.day}/{dt.month}/{dt.year}")

# This method turns datetime objects to strings
print(dt.strftime("%d/%m"))
print("dt2:", dt2, "dt1:", dt1, "(dt2 > dt1):", dt2 > dt1)

# --------------------------------------------------------

dt1 = datetime(2020, 2, 16) + timedelta(days=1)
dt2 = datetime.now()

print("dt1:", dt1)

duration = dt2 - dt1
print(duration)
print("days", duration.days)
# This gives how many seconds do we have in the days (not including hours etc.)
print("seconds", duration.seconds)
# This is total seconds (including hours etc.)
print("total_seconds", duration.total_seconds())
