from pydoc import Doc
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render
from nst import change_image
# Create your views here.
from .models import ImageModel
from django.views.decorators.csrf import csrf_exempt
import os
from user.models import User as UserModel
from rest_framework.response import Response
from rest_framework.decorators import api_view
from image.serializers import ImageSerializer
from datetime import datetime

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.core.files.images import ImageFile

from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
import io
import sys
from base64 import b64encode
import jwt


@csrf_exempt
@api_view(('POST',))
def upload(request):
    if request.method == "POST":
        # try:
        # 1번 사진 / 기본
        first_image = str(request.FILES['photos_0'])
        first_image = "upload_image/" + first_image.replace(" ", "_")
        # 2번 사진 / 명화
        second_image = str(request.FILES['photos_1'])
        second_image = "upload_image/" + second_image.replace(" ", "_")

        # 1번 사진 / 기본
        default_storage.save(f'{first_image}', ContentFile(
            request.FILES['photos_0'].read()))
        # 2번 사진 / 명화
        default_storage.save(f'{second_image}', ContentFile(
            request.FILES['photos_1'].read()))

        ai_result_img, ai_result_name = change_image(
            first_image, second_image)  # 여기에 first_image, second_image 넣어주세요

        ai_result_img.convert('RGB')
        ai_result_img.resize(ai_result_img.size, Image.ANTIALIAS)
        output = io.BytesIO()
        ai_result_img.save(output, format='JPEG', quality=100)
        output.seek(0)
        ImageModel.objects.create(
            user=request.user,
            images=InMemoryUploadedFile(
                output, "ImageField", ai_result_name, 'image/jpeg', sys.getsizeof(output), None),
            title=ai_result_name
        )
        ResultImageId = ImageModel.objects.get(title=ai_result_name).id
        OtherImage = ImageModel.objects.all().exclude(user=request.user)
        return Response({'message': "성공", "other_img": OtherImage, "image_id": ResultImageId, "data": b64encode(open("media/pics/" + ai_result_name, 'rb').read())})
        # except:
        #     return Response({'message': '실패'})


@csrf_exempt
@api_view(('PUT',))
def get_image_info(request):
    if request.method == 'PUT':
        try:
            img_subscription = request.data['img_sub']
            img_user = request.data['img_id']
            ImageToChanage = ImageModel.objects.get(id=img_user)
            ImageToChanage.subscription = img_subscription
            return Response({'message': '성공'})
        except:
            return Response({'message': '실패'})


@csrf_exempt
@api_view(('GET',))
def get_image(request, id):
    if request.method == 'GET':
        print(id)
        try:
            DownloadImage = ImageModel.objects.get(id=id).images
            return Response({DownloadImage})
        except:
            return Response({'message': '실패'})
