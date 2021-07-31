from django.contrib import admin
from .models import Language, Tags, Image

# Register your models here.
admin.site.register(Language)
admin.site.register(Tags)
admin.site.register(Image)
