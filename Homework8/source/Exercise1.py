import datetime
import time

start = time.time();

date_entry = input('Enter a date in YYYY-MM-DD format ')
year, month, day = map(int, date_entry.split('-'))
firstDate = datetime.date(year, month, day)

date_entry = input('Enter a second date in YYYY-MM-DD format ')
year, month, day = map(int, date_entry.split('-'))
secondDate = datetime.date(year, month, day)

end = time.time();


print(str(secondDate - firstDate) + " days have passed between the two dates.")
print("The program executed in " + str(end - start) + " seconds.")
