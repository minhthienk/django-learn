from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
'''
def index(request):
   response = HttpResponse()
   response.writelines('<h1>Xin chào</h1>')
   response.write('Đây là app home')
   return response
'''
def index(request):
   return render(request, 'pages/home.html')

def contact(request):
   return render(request, 'pages/contact.html')


def error(request, exception):
    return render(request, 'pages/error.html', {'message': exception})


from .forms import RegistrationForm
from django.http import HttpResponseRedirect 

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/home/')
    return render(request, 'pages/register.html', {'form': form})




from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/home/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "pages/login.html",
                    context={"form":form})