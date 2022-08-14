import time

print(time.ctime(1000000))  # epoch → ctime() convert a time expressed in seconds since epoch to a readable string
# epoch is when your computer thinks time began (reference point) → .ctime(0)
# Mon Jan 12 10:46:40 1970 is the output since ((1000000)) seconds have passed since
# beginning

print(time.time())  # returns current seconds since epoch

print(time.ctime(time.time()))  # gets current time

time_object = time.localtime()  # creates a time object
# time.strftime(format, time_object) formatting object into readable information

local_time = time.strftime("%B %d, %Y || %H:%M:%S",
                           time_object)  # → access Python's documentation for details on format
print(local_time)  # to output current time as formatted above

time_string = "20 February, 1982"
time_object2 = time.strptime(time_string, "%d %B, %Y")  # converting a string into a time object (unreadable)
print(time_object2)

time_tuple = (2002, 3, 8, 7, 30, 0, 0, 0, 0)  # (Y, m, d, h, m, s, day of week, day of year, daylight savings time)
time_string2 = time.asctime(time_tuple)
print(time_string2)
