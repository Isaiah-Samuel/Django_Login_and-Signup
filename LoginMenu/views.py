from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.\
def landingpage(request):
    return render(request,'landingpage.html')

# def logIn(request):
#     return render(request, 'logIn.html')

def homepage(request):
    return render(request,'homepage.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(password=password).exists() == False:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already in use')
                return redirect('register')

            elif User.objects.filter(first_name=first_name).exists() and User.objects.filter(last_name=last_name).exists():
                messages.info(request, 'Names already in use')
                return redirect('register')

            else:
                user = User.objects.create_user(username=email,first_name=first_name, last_name=last_name, email=email, password=password)
                user.save()
                return redirect('logIn')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html') 

def logIn(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'homepage.html')
        else:
            messages.error(request, 'oops!!!  Invalid email or password')
            return redirect('logIn')
    else:
        return render(request,'logIn.html')