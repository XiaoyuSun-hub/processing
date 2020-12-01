import numpy
import os

from os import walk
import shutil

path = os.getcwd()
# f = []
# for (dirpath, dirnames, filenames) in walk('images'):
#     f.extend(filenames)
#     break

source_dir = r'bag'
path = os.getcwd()

train_dir = os.path.join(path, r'raw/train/gt_polygonized/bag')
test_dir = os.path.join(path, r'raw/test/gt_polygonized/bag')

with open("trainlist1.txt", "r") as f:
    data = f.read().split('\n')
    x_train = numpy.array(data)  # convert array to numpy type array

with open("testlist1.txt", "r") as f2:
    data2 = f2.read().split('\n')
    x_test = numpy.array(data2)  # convert array to numpy type array
# path = os.getcwd()
# os.mkdir(os.path.join(path,train_dir))
# os.mkdir(os.path.join(path,test_dir))
# file_names = os.listdir(source_dir)

for file_name in x_train:
    # shutil.move(os.path.join(source_dir, file_name), train_dir)
    # ENS_259851_467200.tif  geoms_252299_466560.geojson
    if len(file_name)>0:
        jsonName = "geoms_" + file_name[4:-4] + ".geojson"
        destName=file_name[:-4]+".geojson"
        print(jsonName)
        shutil.copyfile(os.path.join(source_dir, jsonName), os.path.join(train_dir, destName))
for file_name in x_test:
    # shutil.move(os.path.join(source_dir, file_name), test_dir)
    if len(file_name)>0:
        jsonName = "geoms_" + file_name[4:-4] + ".geojson"
        destName=file_name[:-4]+".geojson"
        print(jsonName)
        shutil.copyfile(os.path.join(source_dir, jsonName), os.path.join(test_dir, destName))
