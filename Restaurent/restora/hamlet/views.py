from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import ContactForm
from . models import UserContactForm
# Create your views here.
def index(request):
    return render(request, 'common_code/index.html')

# Contact page views
def Contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name_data = form.cleaned_data['name']
            email_data = form.cleaned_data['email']
            message_data = form.cleaned_data['message']
            saveForm = UserContactForm(name=name_data, email=email_data, message=message_data)
            saveForm.save()
            return HttpResponseRedirect('/contact')
        else:
            form = ContactForm()
            
    form_data = {
        'form':form
    }
    return render(request, 'hamlet/contact.html',form_data)


