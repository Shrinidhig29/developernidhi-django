from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.


def home(request):
    # return HttpResponse("This is my homepage (/)")
    context = {'name': 'Nidhi', 'course': 'Django'}
    return render(request, 'home.html', context)


def about(request):
    # return HttpResponse("This is my about page (/about)")
    return render(request, 'about.html')


# def projects(request):
    # return HttpResponse("This is my projects page (/project)")
    # return render(request, 'projects.html')


def contact(request):
    # return HttpResponse("This is my contact page (/contact)")
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        # print(name, email, password, phone)
        contact = Contact(name=name, email=email, password=password, phone=phone)
        contact.save()
        print('the data has been return to the db')
    return render(request, 'contact.html')


def services(request):
    # return HttpResponse("This is my service page (/service)")
    return render(request, 'services.html')
