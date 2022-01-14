from django.urls import path, include
from rest_framework.routers import DefaultRouter
from ititems.views import ItitemsViewSet

app_name = "ititems"

router = DefaultRouter()
router.register("itnews", ItitemsViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
]

