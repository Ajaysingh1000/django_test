from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import File
from .serializers import FileSerializer
from rest_framework import viewsets
import os
from django.conf import settings

import logging
logger = logging.getLogger(__name__)


class FileView(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    
    def get_queryset(self):
        x = os.path.join(settings.BASE_DIR, 'files')
        logger.info(x)
        return super().get_queryset()
