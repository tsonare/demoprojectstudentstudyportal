from  django import forms
from .models import *



class NotesForm(forms.ModelForm):
    user = forms.CharField(widget=forms.HiddenInput())
    
    # user = forms.HiddenField()
    class Meta:
        model = Note
        fields = ['title', 'description','user']
        widgets = {'user': forms.HiddenInput()}
      

    
    