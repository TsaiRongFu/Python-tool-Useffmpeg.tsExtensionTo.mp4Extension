import os

try:
    f = open("./output.txt", "r+", encoding='utf-8')
    lines = f.readlines()
    find = True
except:
    find = False
    print("system：not find .ts extension on current directory")

if find:
    for line in lines:
        os.system(line.strip('\n'))
