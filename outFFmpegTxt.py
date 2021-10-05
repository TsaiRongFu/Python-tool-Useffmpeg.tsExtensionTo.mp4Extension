from os import listdir
from os.path import isfile, isdir, join
mypath = "./"

files = listdir(mypath)

for f in files:
  fullpath = join(mypath, f)
  if isfile(fullpath):
    if(f.find(".ts") != -1):
        oldname = f
        newname = f.replace('.ts', '.mp4')
        f = open("./output.txt", 'a+', encoding='utf-8')
        f.write('sudo ffmpeg -i "{}" -c:v copy -c:a aac "{}"\n'.format(oldname, newname))
        f.close()