
from rest_framework import serializers

from .models import Image


# Querying of apis will be done here.
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('name', 'language', 'tag', 'image_asset')
        model = Image
