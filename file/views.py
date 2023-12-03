# 12 create code for view.py for urls.py sub django app named "file"

from django.shortcuts import render, HttpResponse
from .forms import upload # form class name 
from .models import file_upload

def index(request):

    if request.method == 'POST':
        form = upload(request.POST, request.FILES) # form class name

        print(form.as_p)
        
        if form.is_valid():
            name = form.cleaned_data['file_name']
            the_files = form.cleaned_data['files_data']

            file_upload(file_name=name, my_file=the_files).save()
            
            return HttpResponse("file upload")
        else:
            return HttpResponse('error')

    else:
        
        context = {
            'form':upload() # form class name
        }      
        
        return render(request, 'welcome.html', context)
    

def show_file(request):
    # this for testing 
    all_data = file_upload.objects.all()

    context = {
        'data':all_data 
        }

    return render(request, 'display.html', context)
    
