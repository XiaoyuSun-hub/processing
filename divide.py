from sklearn.model_selection import train_test_split
import numpy
import os
# from os import listdir
# from os.path import isfile, join
# onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
# or you could use os.walk() which will yield two lists for each directory it visits - splitting into files and dirs for you. If you only want the top directory you can break the first time it yields

from os import walk
import shutil
path = os.getcwd()
f = []
for (dirpath, dirnames, filenames) in walk('images'):
    f.extend(filenames)
    break
# with open('listimages.txt', 'w') as filehandle:
#     # filehandle.writelines("%s\n" % place for place in f)
#     filehandle.writelines("%s\n" % place for place in f)



x_train,x_test = train_test_split(f,test_size=0.2)       #test_size=0.5(whole_data)

with open('trainlist1.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % place for place in x_train)
# with open('trainlist1semicolon.txt', 'w') as filehandle:
#     filehandle.writelines("%s;" % place for place in x_train)

with open('testlist1.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % place for place in x_test)
# with open('testlist1semicolon.txt', 'w') as filehandle:
#     filehandle.writelines("%s;" % place for place in x_train)

source_dir = 'images'
train_dir = 'train'
test_dir='test'
# path = os.getcwd()
# os.mkdir(os.path.join(path,train_dir))
# os.mkdir(os.path.join(path,test_dir))
#file_names = os.listdir(source_dir)

for file_name in x_train:
    # shutil.move(os.path.join(source_dir, file_name), train_dir)
    shutil.copyfile(os.path.join(source_dir, file_name), os.path.join(train_dir, file_name))
for file_name in x_test:
    #shutil.move(os.path.join(source_dir, file_name), test_dir)
    shutil.copyfile(os.path.join(source_dir, file_name), os.path.join(test_dir, file_name))
