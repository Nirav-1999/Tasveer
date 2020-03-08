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
# Create your views here.

class MlModelViewset(viewsets.ModelViewSet):
    serializer_class=MlModelSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]

    # def get_queryset(self):
    #     print(self.request.user.mlmodel.all())
    #     return self.request.user.mlmodel.all()

    # def perform_create(self,serializer):
        # print(self.request.data['zipfile'].file)
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
        os.system("python ..\code.py ")
        
        # print(stat)
        # print(arr)
        return Response({
            "Message":"Success",
        })
l=[]
class Images128(APIView):
    def get(self,request):
        x=Images.objects.all()
        print(x)
        return Response({
            'images':x
        },content_type="image/png")

    def post(self,request):
        # print(request)
        for files in request.data.getlist('images'):
            m=Images(image=files)
            m.save()
            
        # for ele in request.data:
        #     print(ele['images'])
        # for i in f:
        #     l.append(i)
        # print(l)
        return Response({
            "Data":"Success"
        })



class ImagesViewset(viewsets.ModelViewSet):
    queryset=Images.objects.all()
    serializer_class=ImageSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]

