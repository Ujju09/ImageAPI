
from rest_framework import generics
from .serializers import ImageSerializer
from .models import Image


# Create your views here.
class ImageList(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


# Adding query params

class ImageDetailList(generics.RetrieveAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
