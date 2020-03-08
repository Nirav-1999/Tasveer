from .models import MlModel,TrainedModel,Images
from rest_framework import serializers
from django.contrib.auth.models import User

class MlModelSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = MlModel
        fields = ('id','zipfile')


class TrainedModelSerializer(serializers.HyperlinkedModelSerializer):
    model = serializers.ReadOnlyField(source='modelfrom.model_name')
    
    class Meta:
        model = MlModel
        fields = ('id','modelfrom','trained_model')

class ImageSerializer(serializers.HyperlinkedModelSerializer):

    # image = serializers.SerializerMethodField()

    class Meta:
        model = Images
        fields = ('image',)

   