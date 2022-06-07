from django import forms
from .models import mrcdata


class MrcPost(forms.ModelForm):
    class Meta:
        model = mrcdata
        fields = ['contents', 'question', 'answer']