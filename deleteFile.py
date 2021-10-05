import os
from os import listdir
from os.path import isfile, isdir, join
mypath = "./"

files = listdir(mypath)

for f in files:
  fullpath = join(mypath, f)
  if isfile(fullpath):
    if(f.find(".ts") != -1):
        os.system('sudo rm "' + f + '"')
        print("Delete：" + f + " - Sussess！")

os.system('sudo rm "outFFmpegTxt.py"')
print("Delete：outFFmpegTxt.py - Sussess！")

os.system('sudo rm "runTermainl.py"')
print("Delete：runTermainl.py - Sussess！")

os.system('sudo rm "output.txt"')
print("Delete：output.txt - Sussess！")

os.system('sudo rm "deleteFile.py"')
print("Delete：delete.py - Sussess！")

os.system('sudo rm "main.py"')
print("Delete：main.py - Sussess！")