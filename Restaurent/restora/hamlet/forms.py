from django import forms 
from django.core import validators

# Contact Form
class ContactForm(forms.Form):
    name = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput())
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':3,'cols':25}))
    