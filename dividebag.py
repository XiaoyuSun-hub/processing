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

dirimage=r"C:\code\processing\EnschedeImageDataset"

source_image= os.path.join(dirimage,"images")
source_json= os.path.join(dirimage,"gt_polygonized","bag")

dirimage2=r"C:\code\processing\EnschedeImageDataset\urbanareabag\raw"
train_dir = os.path.join(dirimage2,"train","gt_polygonized")
valdir=os.path.join(dirimage2,"val","gt_polygonized")
test_dir=os.path.join(dirimage2,"test","gt_polygonized")
itrain_dir = os.path.join(dirimage2,"train","images")
ivaldir=os.path.join(dirimage2,"val","images")
itest_dir=os.path.join(dirimage2,"test","images")
# path = os.getcwd()
# os.mkdir(os.path.join(path,train_dir))
# os.mkdir(os.path.join(path,test_dir))
#file_names = os.listdir(source_dir)

rootdir=r"C:\code\processing\EnschedeImageDataset\newboxurban"

trainlist = os.path.join(rootdir,"trainlist.txt")
vallist = os.path.join(rootdir,"vallist.txt")
testlist = os.path.join(rootdir,"testlist.txt")

with open(trainlist, "r") as f:
    data = f.read().split('\n')
    x_train = numpy.array(data)  # convert array to numpy type array

with open(testlist, "r") as f2:
    data2 = f2.read().split('\n')
    x_test = numpy.array(data2)  # convert array to numpy type array

with open(vallist, "r") as f3:
    data = f3.read().split('\n')
    x_val = numpy.array(data)  # convert array to numpy type array



for file_name in x_train:
    # shutil.move(os.path.join(source_dir, file_name), train_dir)
    shutil.copyfile(os.path.join(source_image, file_name), os.path.join(itrain_dir, file_name))
    shutil.copyfile(os.path.join(source_json, file_name[0:-4] + ".geojson"), os.path.join(train_dir, file_name[0:-4] + ".geojson"))
    # shutil.copyfile(os.path.join(results_json, file_name), os.path.join(train_dir, file_name))

for file_name in x_test:
    #shutil.move(os.path.join(source_dir, file_name), test_dir)
    shutil.copyfile(os.path.join(source_image, file_name), os.path.join(itest_dir, file_name))
    shutil.copyfile(os.path.join(source_json, file_name[0:-4] + ".geojson"), os.path.join(test_dir, file_name[0:-4] + ".geojson"))

for file_name in x_val:
    #shutil.move(os.path.join(source_dir, file_name), test_dir)
    shutil.copyfile(os.path.join(source_image, file_name), os.path.join(ivaldir, file_name))
    shutil.copyfile(os.path.join(source_json, file_name[0:-4] + ".geojson"), os.path.join(valdir, file_name[0:-4] + ".geojson"))
