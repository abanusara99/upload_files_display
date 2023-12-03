# 10 - create manual urls.py in sub django app "file"
# 11 - add code below
from django.urls import path

from . import views


urlpatterns = [
    
    path('', views.index, name="homepage"),
    # 23 - files that uploaded will be displayed with this urls
    path('view', views.show_file, name="display") 
        
]