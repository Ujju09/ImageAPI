from django.db import models


# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=50, default='English')

    def __str__(self):
        return self.name


class Tags(models.Model):
    tag_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.tag_name


class Image(models.Model):
    name = models.CharField(max_length=1000)
    image_asset = models.FileField(upload_to='assets/')
    language = models.ForeignKey("Language", on_delete=models.SET_DEFAULT, default='English')
    tag = models.ForeignKey("Tags", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
