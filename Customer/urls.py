from django.urls import path, include
from rest_framework import routers

from Customer.views import UserViewSet

router = routers.DefaultRouter()

router.register("customer", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

app_name = "Customer"
