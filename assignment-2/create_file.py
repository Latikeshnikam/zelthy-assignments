import time
import os

input_text = input("Please enter file contents?")
timestr = time.strftime("%d-%m-%Y")
filename = "/file_createTime_" + time.strftime("%H:%m:%s") + '.txt'
path = "./" + timestr
try:
    os.makedirs(path, exist_ok=True)
    f = open(path + filename, 'w+')
    f.write(input_text)
    f.close()
except OSError as error:
    print(error)
