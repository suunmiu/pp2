#1

import datetime
x = datetime.datetime.now().date() - datetime.timedelta(days = 5)

print("five days from current date:", x)

#2

import datetime 
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
tomorrow = datetime.datetime.now() + datetime.timedelta(days = 1)
today = datetime.datetime.now()
print("yesterday:", yesterday)
print("today:", today)
print("tomorrow:", tomorrow)

#3
import datetime
x = datetime.datetime.now()
datetime_without_microseconds = x.replace(microsecond=0)
print("date without microsec:", datetime_without_microseconds)

#4
import datetime

def date_difference_in_seconds(date1, date2):

    datetime1 = datetime.datetime.strptime(date1, "%Y-%m-%d %H:%M:%S")
    datetime2 = datetime.datetime.strptime(date2, "%Y-%m-%d %H:%M:%S")
    
    difference_seconds = abs((datetime2 - datetime1).total_seconds())

    return difference_seconds

date_str1 = str(input())

date_str2 = "2022-01-02 14:30:00"

difference_seconds = date_difference_in_seconds(date_str1, date_str2)

print(f"Difference in seconds between {date_str1} and {date_str2}: {difference_seconds} seconds")

