# 15 - add models.py from sub django app named "file"
# 16 - in terminal of myups - makemigrations and migrate must be to used to upload new changes or sql data based changes


from django.db import models

# Create your models here.

class file_upload(models.Model):
    ids = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    my_file = models.FileField(upload_to='')
    
    # 21 - if the file_uploads from admin/ page is not shown , add 
    def __str__(self):
        return self.file_name 
    
    