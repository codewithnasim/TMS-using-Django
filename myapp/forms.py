from django import forms
from .models import  Usr,Proffesional,Servicesreq
class Bal(forms.ModelForm):
    class meta:
        model=Usr,Proffesional,Servicesreq
        fields="__all__"