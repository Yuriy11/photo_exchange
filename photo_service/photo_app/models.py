from django.db import models

# Create your models here.


class Picture(models.Model):
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/', null=False)