import tensorflow.keras.layers as Layers
import pickle
import tensorflow.keras.activations as Actications
import tensorflow.keras.models as Models
import tensorflow.keras.optimizers as Optimizer
import tensorflow.keras.metrics as Metrics
import tensorflow.keras.utils as Utils
from keras.utils.vis_utils import model_to_dot
import os
import pickle
import matplotlib.pyplot as plot
import cv2
import numpy as np
from sklearn.utils import shuffle
from sklearn.metrics import confusion_matrix as CM
from random import randint
def train(Images,Labels):
	model = Models.Sequential()
	model.add(Layers.Conv2D(200,kernel_size=(3,3),activation='relu',input_shape=(150,150,3)))
	model.add(Layers.Conv2D(180,kernel_size=(3,3),activation='relu'))
	model.add(Layers.MaxPool2D(5,5))
	model.add(Layers.Conv2D(180,kernel_size=(3,3),activation='relu'))
	model.add(Layers.Flatten())
	model.add(Layers.Dense(180,activation='relu'))
	model.compile(optimizer=Optimizer.Adam(lr=0.0001),loss='sparse_categorical_crossentropy',metrics=['accuracy'])
	trained = model.fit(Images,Labels,epochs=35,validation_split=0.30)
	return trained
