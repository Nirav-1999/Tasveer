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


urlpatterns = [
    url(r'',include(router.urls)),
]