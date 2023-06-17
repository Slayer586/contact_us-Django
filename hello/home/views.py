from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact
# Create your views here.

def contactus(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        subject= request.POST.get('subject')
        contact = Contact(firstname=firstname,lastname=lastname,email=email,phone=phone,subject=subject,date=datetime.today())
        contact.save()
    return render(request, 'contactus.html')    