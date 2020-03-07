def Conv2D():
    f.write("model.add(Layers.Conv2D(180,kernel_size=(3,3),activation='relu'))")

with open('model.py','w+') as f:
    f.write("model = Models.Sequential()\n")
    Conv2D()


