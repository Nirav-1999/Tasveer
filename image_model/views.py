from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from .models import MlModel, TrainedModel
from .serializers import MlModelSerializer, TrainedModelSerializer
import zipfile
import io
import os

# Create your views here.

class MlModelViewset(viewsets.ModelViewSet):
    serializer_class=MlModelSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]

    def get_queryset(self):
        print(self.request.user.mlmodel.all())
        return self.request.user.mlmodel.all()

    def perform_create(self,serializer):
        print(type(self.request.data['zipfile']))
        # print(str(self.request.data['zipfile']) in os.listdir('D:\codeshastra6.0\codeshastra6.0\media') )
        # print(os.listdir('D:\codeshastra6.0\codeshastra6.0\media'))
        serializer.save(user=self.request.user)
        z = zipfile.ZipFile(self.request.data['zipfile'].file)
        z.extractall()
        


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
