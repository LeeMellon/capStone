from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.contrib.auth import authenticate


# Create your views here.

def register(request):
    """
    User Registration View "sign up"
    
    """
    if request.method == 'GET':
        form = CustomUserCreationForm()
    elif request.method == 'POST':
        form = CustomUserCreationForm( data=request.POST )

        if form.is_valid():
            user = form.save( commit=False )
            # we can make any last second changes to the user
            user.save()
            return redirect( '/' )

    context = {'form': form}
    return render( request, 'register.html', context )


def login(request):
    '''
    user login 
    
    '''
    if request.method == "GET":
        form = AuthenticationForm()
    #handle POST
    elif request.method == "POST":
        #get form data dictionary POST
        username = request.POST.get('username')
        password = request.POST.get('password')
    #form validation
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #check username/password is correct
            user = authenticate(username=username, password=password)
            if user:
                #login(session)
                django_login(request, user)
                #redirect
                return redirect('/')

    context={'form':form}
    return render( request, 'login.html', context)

def logout(request):
    django_logout(request)