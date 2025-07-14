from django.forms import ModelForm
from .models import Announcement
from django import forms

class AnnouncementForm(ModelForm):
    class Meta:
        model = Announcement
        fields= ['title','textField']
        labels= {'title':'Başlık',
                 'textField':'Metin'}
        
