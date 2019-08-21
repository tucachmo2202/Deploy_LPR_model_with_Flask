import pickle
import cv2
import numpy as np 
from matplotlib import pyplot as plt 
import os
from sklearn.neighbors import KNeighborsClassifier

train_folder = 'Dataset/Train'
train_data = []
labels = []
real_label = {}
for class_ in os.listdir(train_folder):
    [this_class,this_label] = class_.split('.')
    class_folder = os.path.join(train_folder,class_)
    real_label[int(this_class)]=this_label
    for img_name in os.listdir(class_folder):
        img_path = os.path.join(class_folder,img_name)
        img = cv2.imread(img_path,0)
        img = np.reshape(np.array(img),-1)
        train_data.append(img)
        labels.append(int(this_class))

print('loading Data Done !!!')



neigh = KNeighborsClassifier(n_neighbors = 1)
neigh.fit(train_data,labels)

filename = 'model.sav'
pickle.dump(neigh, open(filename, 'wb'))
print("Save successfully!")


