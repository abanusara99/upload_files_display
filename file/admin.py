# 20- add  file_uploads in as user in admin.py and admin/ page 
from django.contrib import admin

from .models import file_upload
# Register your models here.

admin.site.register(file_upload)