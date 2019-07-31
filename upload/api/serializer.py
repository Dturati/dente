from rest_framework import serializers
from upload.models import UploadImage

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        Model = UploadImage
        fields = ('image')