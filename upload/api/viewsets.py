from django.http import HttpResponse, FileResponse
from rest_framework import status
import os
from rest_framework.decorators import api_view
from rest_framework.response import Response

from upload.api.serializer import ImageSerializer
from upload.models import UploadImage
from processa.open_cv.processa1 import processa1
from django.core.files import File
import base64


@api_view(['GET'])
def processa_dente(request):
    if request.method == 'GET':
        return Response('GET')

@api_view(['POST'])
def upload(resquest):
    serializer_class = ImageSerializer
    # queryset = UploadImage
    if resquest.method == 'POST':
        foto = resquest.FILES['image']
        # image = UploadImage.objects.create(image=foto)
        content_type = 'image/' + '*'
        return FileResponse(open('media/image/imgRgb.jpg', 'rb'), content_type=content_type)
