from django.db import models
from user.models import User
# Create your models here.


class ImageModel(models.Model):
    title = models.CharField(max_length=256)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/',blank=True, null=True)
    # like = models.ArrayField(null=False)

    # 제목으로 파일을 구분할 수 있게
    def __str__(self):
        return str(self.title)
