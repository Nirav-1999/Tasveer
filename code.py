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
from IPython.display import SVG
import matplotlib.gridspec as gridspec
def train(images,labels):
	model = Models.Sequential()
	model.add(Layers.Conv2D(123,kernel_size=(3,3),activation='relu',input_shape=(124,123,3)))
	model.add(Layers.Flatten())
	model.add(Layers.Dense(123,activation='sigmoid'))
	model.add(Layers.Conv2D(124,kernel_size=(3,3),activation='sigmoid'))
	model.add(Layers.MaxPool2D(4,4))
	model.add(Layers.Conv2D(4546,kernel_size=(3,3),activation='sigmoid'))
	model.compile(optimizer=Optimizer.Adam(lr=0.0001),loss='sparse_categorical_crossentropy',metrics=['accuracy'])
	return model