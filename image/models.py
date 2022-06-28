from django.db import models
from user.models import CustomUser
# Create your models here.
class Image(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(null=False)
    name = models.CharField(max_length=256)
    like = models.ArrayField(null=False)
