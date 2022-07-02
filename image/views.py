from django.shortcuts import render
from nst import change_image
# Create your views here.
from .models import ImageModel
import os

def upload(request):
    if request.method == "POST":
        images = request.FILES.getlist("images")

        for img in images:
            ImageModel.objects.create(images=img)
    images = ImageModel.objects.all() #input 이미지 url 불러옴
    images_slice = ImageModel.objects.all().order_by('-timestamp')[0:2] # 가장 최근에 넣은 input 이미지 url
    # print(images_slice)
    input_images_list= []
    for image_num in (0,2):
        try:
            images_values = ImageModel.objects.values('images').order_by('-timestamp')[image_num]['images']  
            input_images_list.append(images_values)
        except:
            pass
    print(input_images_list)
    try:
        result_image_path=change_image(input_images_list[0],input_images_list[1])
        result_image_path
        # change_image(input_images_list[0],input_images_list[1])
        file_list = os.listdir('./')
        print(file_list)
        print ("Result is ", result_image_path)
        return render(request, "main.html", {"images": images_slice, "result_image_path": result_image_path})
    except:
        return render(request, "main.html")