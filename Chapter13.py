import time
#13.1 Write the current date as a string to the text file today.txt
now = time.time()
time_string = time.ctime(now)
print("The current time is ", time_string)
write_file = open("today.txt", "w")
write_file.write(time_string)
write_file.close()
print("")
#13.2 Read the text file today.txt into the string today_string.
read_file = open("today.txt", "r")
today_string = read_file.read()
print("Time read from the text file is ", today_string)
read_file.close()
print("")
#13.3 Parse the date from today_string.
formatTime = "%a %b %d %I:%M:%S %Y"
print("Parse the date:", time.strptime(today_string, formatTime))