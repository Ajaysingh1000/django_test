
from django.contrib import admin
from django.urls import path
from .views import FileView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'files', FileView, basename='file')

urlpatterns = router.urls
