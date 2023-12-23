from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

def index(request):
    context={
        'variable1' : "Life is rough!",
        'variable2' : "Life is Is beautiful!"
    }
    messages.success(request, "this is a text mesage")
    # return HttpResponse("This is home page")
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email= email, phone=phone, desc = desc, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been send.")
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')