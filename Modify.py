import os
import shutil

inputdir = '/home/user/input'
outputdir = '/home/user/output'



for filename in os.listdir(inputdir):
    if os.path.splitext(filename)[1] == ".jpg":
        with open('test.txt', 'a') as file:
            file.write('<img src="documents/photos/{}" alt="Something or another">'.format(filename))
        shutil.copy2(os.path.join(inputdir, filename), outputdir)