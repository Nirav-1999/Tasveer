from django.contrib import admin
from .models import TrainedModel,MlModel

# Register your models here.
admin.site.register(TrainedModel)
admin.site.register(MlModel)