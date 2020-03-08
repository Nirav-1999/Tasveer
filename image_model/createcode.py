
# def Conv2D(*args):
#     args=args[0]
#     if 'Convolutional' not in seen:
#         f.write("model.add(Layers.Conv2D({},kernel_size=({},{}),activation='{}',input_shape=({},{},3)))\n".format(args['number_of_filters'],args['kernel_size_x'],args['kernel_size_y'],args['activation'],args['input_shape_x'],args['input_shape_y']))
#     else:
#         f.write("model.add(Layers.Conv2D({},kernel_size={},activation='{}'))\n".format(args['number_of_filters'],args['kernel_size_x'],args['kernel_size_y'],args['activation']))

# def MaxPool2D(*args):
#     f.write("model.add(Layers.MaxPool2D){}\n".format(args['kernel_size_x'],args['kernel_size_y']))
#     # print(args)

# def Dense(*args):
#     args=args[0]
#     if 'Dense' in seen:
#         f.write("model.add(Layers.Dense({},activation='{}'))\n".format(args['number_of_nodes'],args['activation']))
#     else:
#         f.write("model.add(Layers.Flatten())\n")
#         f.write("model.add(Layers.Dense({},activation='{}'))\n".format(args['number_of_nodes'],args['activation']))

# def Dropout(*args):
#     f.write('model.add(Layers.Dropout(rate={}))\n'.format(args[0]))

# switcher={
#     'Convolutional':Conv2D,
#     'MaxPooling':MaxPool2D,
#     'Dense':Dense,
#     'Dropout':Dropout
# }
# seen=set()
# f=open('code.py','w+')
def create(arr,stat):
    dropout=stat['dropout_rate']
    print(stat)
    seen=set()
    def Conv2D(*args):
        args=args[0]
        if 'Convolutional' not in seen:
            f.write("\tmodel.add(Layers.Conv2D({},kernel_size=({},{}),activation='{}',input_shape=({},{},3)))\n".format(args['number_of_filters'],args['kernel_size_x'],args['kernel_size_y'],args['activation'],args['input_shape_x'],args['input_shape_y']))
        else:
            f.write("\tmodel.add(Layers.Conv2D({},kernel_size=({},{}),activation='{}'))\n".format(args['number_of_filters'],args['kernel_size_x'],args['kernel_size_y'],args['activation']))

    def MaxPool2D(*args):
        args=args[0]
        f.write("\tmodel.add(Layers.MaxPool2D({},{}))\n".format(args['kernel_size_x'],args['kernel_size_y']))
        # print(args)

    def Dense(*args):
        args=args[0]
        if 'Dense' in seen:
            f.write("\tmodel.add(Layers.Dense({},activation='{}'))\n".format(args['number_of_nodes'],args['activation']))
        else:
            f.write("\tmodel.add(Layers.Flatten())\n")
            f.write("\tmodel.add(Layers.Dense({},activation='{}'))\n".format(args['number_of_nodes'],args['activation']))

    def Dropout(*args):
        f.write('\tmodel.add(Layers.Dropout(rate={}))\n'.format(dropout))
        
    switcher={
    'Convolutional':Conv2D,
    'MaxPooling':MaxPool2D,
    'Dense':Dense,
    'Dropout':Dropout
}
    with open('code.py','w+') as f:
    
        f.write("""import tensorflow.keras.layers as Layers
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
def train(images,labels):\n""")
        f.write("\tmodel = Models.Sequential()\n")
        # l=['Convolutional','Convolutional','MaxPool2D','Dense','Dropout']
        l=[]
        for i in arr:
            l.append(i['name'])
        # print(l)
        # x=[(200,(3,3),'relu',(150,150,3)),(180,(3,3),'relu'),((5,5)),(180,'relu'),(0.5)]
        for i in range(len(l)):
            switcher.get(l[i])(arr[i])
            seen.add(l[i])
        f.write("\tmodel.compile(optimizer=Optimizer.Adam(lr={}),loss='sparse_categorical_crossentropy',metrics=['accuracy'])\n".format(stat['learning_rate']))
        f.write("\treturn model")
    



