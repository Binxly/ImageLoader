import os
import shutil

inputdir = 'C:\user\Photos\input'
#path of the folder containing jpgs to move
outputdir = 'C:\user\Photos\output'
#path of folder to put jpgs

file = open("test.txt", "a")
#opens text file named test.txt in append mode, text file must exist

for filename in os.listdir(inputdir):
#iterates through every file in indputdir, stores file name in filename variable
    if os.path.splitext(filename)[1] == ".jpg":
    #checks if file extension is .jpg. if not, skips file
        file.write('<img src="documents/photos/{}" alt="Example">'.format(filename))
        #writes img tag to new line of text.txt, {} is placeholder which is filled by filename variable of the .format(filename) syntax
        shutil.copy2(os.path.join(inputdir, filename), outputdir)
        #copies file from inputdir path to outputdir path

file.close()
