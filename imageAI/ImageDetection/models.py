from django.db import models

class Data(models.Model):
    image_file = models.ImageField()
    xml_file = models.FileField()

class Image_Details(models.Model):
    imagename = models.CharField(max_length=300)
    objectname = models.CharField(max_length=150)
    xmin = models.IntegerField()
    xmax = models.IntegerField()
    ymin = models.IntegerField()
    ymax = models.IntegerField()
    timestamp = models.DateField(auto_now_add=True)
