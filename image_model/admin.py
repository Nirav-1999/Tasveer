from django.contrib import admin
from .models import TrainedModel,MlModel,Images

# Register your models here.
admin.site.register(TrainedModel)
admin.site.register(MlModel)
admin.site.register(Images)