from  django import forms
from .models import *


class Notesform(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'description']



    
    