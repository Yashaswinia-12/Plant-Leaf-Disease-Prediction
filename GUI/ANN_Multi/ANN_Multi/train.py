from PyQt5 import QtCore, QtGui, QtWidgets
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

data = []
labels = []
classes = 4
cur_path = os.getcwd()  

classs = {
    0: "Kingfisher",
    1: "Parrot",
    2: "Peacock",
    3: "Pigeon"
}

print("Obtaining Images & its Labels..............")
for i in range(classes):
    path = os.path.join(cur_path, 'my_dir/', str(i))
    images = os.listdir(path)

    for a in images:
        try:
            image = Image.open(path + '/' + a)
            image = image.resize((30, 30))
            image = np.array(image)
            data.append(image)
            labels.append(i)
            print("{0} Loaded".format(a))
        except:
            print("Error loading image")

print("Dataset Loaded")

data = np.array(data)
labels = np.array(labels)

print(data.shape, labels.shape)

data = data / 255.0

X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=0.2, random_state=42)

print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)

y_train = to_categorical(y_train, classes)
y_test = to_categorical(y_test, classes)

print("Training under process with ANN...")

model = Sequential()
model.add(Flatten(input_shape=X_train.shape[1:])) 
model.add(Dense(512, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.3))
model.add(Dense(classes, activation='softmax')) 

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

history = model.fit(X_train, y_train, batch_size=32, epochs=100, validation_data=(X_test, y_test))

model.save("my_model_ann.h5")
print("Saved ANN Model")
