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
	model.add(Layers.Conv2D(124,kernel_size=(3,3),activation='Relu',input_shape=(125,125,3)))
	model.add(Layers.Flatten())
	model.add(Layers.Dense(10,activation='Sigmoid'))
	model.compile(optimizer=Optimizer.Adam(lr=0.0001),loss='sparse_categorical_crossentropy',metrics=['accuracy'])
	return model