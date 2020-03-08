
def Conv2D(*args):
    # print(args[0][0])
    if 'Convolutional' not in seen:
        f.write("model.add(Layers.Conv2D({},kernel_size={},activation='{}',input_shape={}))\n".format(args[0][0],args[0][1],args[0][2],args[0][3]))
    else:
        f.write("model.add(Layers.Conv2D({},kernel_size={},activation='{}'))\n".format(args[0][0],args[0][1],args[0][2]))

def MaxPool2D(*args):
    f.write("model.add(Layers.MaxPool2D){}\n".format(args[0]))
    # print(args)

def Dense(*args):
    if 'Dense' in seen:
        f.write("model.add(Layers.Dense({},activation='{}'))\n".format(args[0][0],args[0][1]))
    else:
        f.write("model.add(Layers.Flatten())\n")
        f.write("model.add(Layers.Dense({},activation='{}'))\n".format(args[0][0],args[0][1]))

def Dropout(*args):
    f.write('model.add(Layers.Dropout(rate={}))\n'.format(args[0]))

switcher={
    'Convolutional':Conv2D,
    'MaxPool2D':MaxPool2D,
    'Dense':Dense,
    'Dropout':Dropout
}
seen=set()

def create(arr,stat):
    with open('model.py','w+') as f:
        
        f.write("""import tensorflow.keras.layers as Layers
    import tensorflow.keras.activations as Actications
    import tensorflow.keras.models as Models
    import tensorflow.keras.optimizers as Optimizer
    import tensorflow.keras.metrics as Metrics
    import tensorflow.keras.utils as Utils
    from keras.utils.vis_utils import model_to_dot
    import os
    import matplotlib.pyplot as plot
    import cv2
    import numpy as np
    from sklearn.utils import shuffle
    from sklearn.metrics import confusion_matrix as CM
    from random import randint
    from IPython.display import SVG
    import matplotlib.gridspec as gridspec\n""")
        f.write("model = Models.Sequential()\n")
        l=['Convolutional','Convolutional','MaxPool2D','Dense','Dropout']
        x=[(200,(3,3),'relu',(150,150,3)),(180,(3,3),'relu'),((5,5)),(180,'relu'),(0.5)]
        for i in range(len(l)):
            switcher.get(l[i])(x[i])
            seen.add(l[i])
        f.write("model.compile(optimizer=Optimizer.Adam(lr=0.0001),loss='sparse_categorical_crossentropy',metrics=['accuracy'])\n")




