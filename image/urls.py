from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.upload, name="upload"),
    path("save/", views.get_image_info, name="getImageInfo"),
    path("download/<id>", views.get_image_info, name="getImageInfo"),
]

# + static(
#     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
# )
