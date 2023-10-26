''' 
-------------------------[Dates]-------------------------
- Python has a built-in module called datetime to help you work with dates and times.
- datetime module has classes for manipulating dates and times.

- datetime.datetime.now() returns the current local date and time.
- datetime.datetime.today() returns the current local date and time.
- datetime.datetime.utcnow() returns the current UTC date and time.
- datetime.datetime.fromtimestamp() returns the local date and time corresponding to the POSIX timestamp.
- datetime.datetime.utcfromtimestamp() returns the UTC date and time corresponding to the POSIX timestamp.
- datetime.datetime.fromordinal() returns the date corresponding to the proleptic Gregorian ordinal.
- datetime.datetime.combine() returns a new datetime object whose date components are equal to the given date object’s, and whose time components and tzinfo attributes are equal to the given time object’s.
- datetime.datetime.strptime() returns a datetime corresponding to date_string, parsed according to format.
- datetime.datetime.date() returns the date part.
- datetime.datetime.time() returns the time part, with tzinfo None.

- the datetime() class requires three parameters to create a date: year, month, day.
- the datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

- the strftime() method takes one or more format codes as an argument and returns a formatted string based on it.

'''
import datetime
x = datetime.datetime.now()
print(x)

x = datetime.datetime.today()
print(x)

# the datetime() class requires three parameters to create a date: year, month, day.
x = datetime.datetime(2020 , 5 , 17)
print(x)

# the datetime() class also takes parameters for time and timezone (hour, minute, second, microsecond, tzone), but they are optional, and has a default value of 0, (None for timezone).

x = datetime.datetime(2020 , 5 , 17 , 12 , 30 , 45 , 100)
print(x)

# the strftime() method takes one or more format codes as an argument and returns a formatted string based on it.
x = datetime.datetime(2018 , 6 , 1)
# %B - month full name
print(x.strftime("%B"))
# %A - weekday full name
print(x.strftime("%A"))
# %a - weekday short name
print(x.strftime("%a"))
print(x.strftime("%b"))
print(x.strftime("%d"))
print(x.strftime("%m"))
print(x.strftime("%y"))
print(x.strftime("%Y"))
print(x.strftime("%H"))
print(x.strftime("%I"))
print(x.strftime("%p"))
print(x.strftime("%M"))
print(x.strftime("%S"))
print(x.strftime("%f"))
print(x.strftime("%z"))
print(x.strftime("%Z"))
print(x.strftime("%j"))
print(x.strftime("%U"))
print(x.strftime("%W"))
print(x.strftime("%c"))
print(x.strftime("%x"))
print(x.strftime("%X"))
print(x.strftime("%%"))

    
