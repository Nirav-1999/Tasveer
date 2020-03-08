from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
# from rest_framework
from django.http import HttpResponseRedirect
from .permissions import IsOwnerOrReadOnly
from .models import MlModel, TrainedModel,Images
from .serializers import MlModelSerializer, TrainedModelSerializer,ImageSerializer
import os
from .createcode import create
import zipfile
# Create your views here.


def get_images(directory):
    Images = []
    Labels = []  # 0 for Building , 1 for forest, 2 for glacier, 3 for mountain, 4 for Sea , 5 for Street
    label = 0
    
    for labels in os.listdir(directory): #Main Directory where each class label is present as folder name.
        if labels == 'glacier': #Folder contain Glacier Images get the '2' class label.
            label = 2
        elif labels == 'sea':
            label = 4
        elif labels == 'buildings':
            label = 0
        elif labels == 'forest':
            label = 1
        elif labels == 'street':
            label = 5
        elif labels == 'mountain':
            label = 3
        
        for image_file in os.listdir(directory+labels): #Extracting the file name of the image from Class Label folder
            image = cv2.imread(directory+labels+r'/'+image_file) #Reading the image (OpenCV)
            image = cv2.resize(image,(150,150)) #Resize the image, Some images are different sizes. (Resizing is very Important)
            Images.append(image)
            Labels.append(label)
    
    return shuffle(Images,Labels,random_state=817328462) #Shuffle the dataset you just prepared.

def get_classlabel(class_code):
    labels = {2:'glacier', 4:'sea', 0:'buildings', 1:'forest', 5:'street', 3:'mountain'}
    
    return labels[class_code]

class MlModelViewset(viewsets.ModelViewSet):
    serializer_class=MlModelSerializer

    # def get_queryset(self):
    #     print(self.request.user.mlmodel.all())
    #     return self.request.user.mlmodel.all()

    def perform_create(self,serializer):
        print(self.request.data['zipfile'].file)
        z = zipfile.ZipFile(self.request.data['zipfile'].file)
        z.extractall()
        # print(str(self.request.data['zipfile']) in os.listdir('D:\codeshastra6.0\codeshastra6.0\media') )
        # print(os.listdir('D:\codeshastra6.0\codeshastra6.0\media'))
        # serializer.save()#user=self.request.user)

class TrainedModelViewset(viewsets.ModelViewSet):
    serializer_class=TrainedModelSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]

    def get_queryset(self):#request):
        # x=MlModel.objects.get(model_name=request.data['model_name'])
        
        print(self.request.query_params)
        print("######################################")
        # print(x.trained_model)
        return TrainedModel.modelfrom.trained_model

    # def perform_create(self,serializer):
    #     serializer.save(modelfrom=)
# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer


class Zip(APIView):
    def post(self,request):
        f=request.FILES['zipfile']
        print(request.FILES)
        m=MlModel(zipfile=f)
        m.save()
        return Response({
            "Uploaded":"Success"
        })
        # return HttpResponseRedirect(redirect_to='localhost:3000/dashboard')

class Parameters(APIView):
    def post(self,request):
        stat=request.data['var1']
        arr=request.data['temp']
        # print(request.data)
        # print(request.data.keys())
        create(arr,stat)
        from .code import train
        Images, Labels = get_images('../input/seg_train/seg_train/') #Extract the training images from the folders.
        Images = np.array(Images) #converting the list of images to numpy array.
        Labels = np.array(Labels)
        train(Images,Labels)

        
        # print(stat)
        # print(arr)
        return Response({
            "Message":"Success",
        })
l=[]
class Images128(APIView):

    def post(self,request):
       
        for files in request.data.getlist('images'):
            m=Images(image=files)
            m.save()
            
    
        return Response({
            "Data":"Success"
        })
# l=[]
# class Images128(APIView):
#     def get(self,request):
#         x=Images.objects.all()
#         print(x)
#         return Response({
#             'images':x
#         },content_type="image/png")

#     def post(self,request):
#         # print(request)
#         for files in request.data.getlist('images'):
#             m=Images(image=files)
#             m.save()
            
#         # for ele in request.data:
#         #     print(ele['images'])
#         # for i in f:
#         #     l.append(i)
#         # print(l)
#         return Response({
#             "Data":"Success"
#         })



class ImagesViewset(viewsets.ModelViewSet):
    queryset=Images.objects.all()
    print(len(queryset))
    serializer_class=ImageSerializer
    permission_classes=[permissions.AllowAny,]

