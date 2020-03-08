from django.conf.urls import url
from django.urls import include
# from rest_framework_swagger.views import get_swagger_view
# from rest_framework.schemas import get_schema_view
from rest_framework.routers import DefaultRouter
from . import views


app_name = "image_model"
# router=SimpleRouter()
router = DefaultRouter()
router.register(r"mymodels", views.MlModelViewset,base_name="MyModel")
router.register(r"trainedmodel", views.TrainedModelViewset,base_name="TrainedModel")
router.register(r"images", views.ImagesViewset,base_name="ImageModel")


urlpatterns = [
    url(r'',include(router.urls)),
    url(r'zipfile',views.Zip.as_view()),
    url(r'parameters',views.Parameters.as_view()),
    url(r'imagepost',views.Images128.as_view()),

]
