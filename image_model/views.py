from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly
from .models import MlModel, TrainedModel
from .serializers import MlModelSerializer, TrainedModelSerializer
import zipfile
import io

# Create your views here.

class MlModelViewset(viewsets.ModelViewSet):
    serializer_class=MlModelSerializer
    permission_classes=[permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,]

    def get_queryset(self):
        print(self.request.user)
        return self.request.user.all()

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
        z = zipfile.ZipFile(io.BytesIO(self.request.data['zipfile'].file))
        print(z.infolist()[0])

        



# class UserViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=UserSerializer
