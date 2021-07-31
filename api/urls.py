from django.urls.conf import re_path

from .views import ImageList, ImageDetailList

urlpatterns = [
    re_path(r'assets/all', ImageList.as_view(), name="assets"),
    re_path(r'^assets/(?P<pk>[0-9]+)$', ImageDetailList.as_view(), name="image-detail"),
]
