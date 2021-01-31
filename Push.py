import os
import shutil

#path of the folder containing jpgs to move
inputdir = '/home/user/input'
#path of folder to put jpgs
outputdir = '/home/user/output'

#iterates through every file in indputdir, stores file name in filename variable
for filename in os.listdir(inputdir):
    if os.path.splitext(filename)[1] == ".jpg": #checks if file extension is .jpg. if not, skips file
        with open('test.txt', 'a') as file: #opens text file named test.txt in append mode, text file must exist
            file.write('<img src="documents/photos/{}" alt="Something or another">'.format(filename)) #writes img tag to new line of text.txt, {} is placeholder which is filled
            #by filename variable of the .format(filename) syntax
        shutil.copy2(os.path.join(inputdir, filename), outputdir) #copies file from inputdir path to outputdir path
