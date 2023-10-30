from django.shortcuts import render

# Create your views here.

def ItalyPizzaMenu(request):
    return render(request, 'fooditem/italypizza.html')
