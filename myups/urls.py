"""
URL configuration for myups project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings             # 5
from django.conf.urls.static import static   # 6

# 5 and 6 are import folders from settings.py and static
urlpatterns = [
    path('admin/', admin.site.urls), # 17 - same termainal, createusersuper for username and password of "admin/" page and add username, email, password, confirm pwd and say y for yes
    path('', include('file.urls')) # 7
  
]

# 7 is urls of sub to main django app, 8 AND 9 ARE static and media folder roots
# 22 - admin/ the folders will be stored in file_upload user of admin/ page and create automatic " media" folder and display the uploaded files in "media" folder

urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT) # 8

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #9 
