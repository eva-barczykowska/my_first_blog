from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]

# """mysite URL Configuration

# [...]
# """
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

