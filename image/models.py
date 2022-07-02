from django.db import models
from user.models import User as UserModel
from datetime import datetime
# Create your models here.


class ImageModel(models.Model):
    title = models.CharField(max_length=256)
    timestamp = models.DateTimeField(default=datetime.now())
    # like = models.ArrayField(null=False)
    # user = models.ForeignKey(UserModel, on_delete=models.CASCADE, null=False)
    images = models.FileField()
# 제목으로 파일을 구분할 수 있게
    def __str__(self):
        return str(self.title)
