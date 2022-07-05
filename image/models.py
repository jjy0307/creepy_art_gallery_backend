from django.db import models
from user.models import User as UserModel
from datetime import datetime
from django.utils import timezone
# Create your models here.


class ImageModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    timestamp = models.DateTimeField(default=datetime.now(tz=timezone.utc))
    subscription = models.TextField(max_length=500, blank=True)
    images = models.FileField(upload_to='pics')
# 제목으로 파일을 구분할 수 있게

    def __str__(self):
        return str(self.title)
