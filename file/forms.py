# 14 add form.py manual file in sub django app named "file" and write code

from django import forms

class upload(forms.Form):
    file_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    files_data = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))