from tkinter import messagebox,Tk
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.
#from login.forms import *
from django import forms
from .views import *
#from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
#from .forms import *
from django.contrib.auth import authenticate, login, logout
#from register.forms import *
from signup.models import *
from .models import *

import p2p_chat.classes.client as client
import p2p_chat.classes.server as server
from p2p_chat.p2p_chat_ import *

@csrf_protect
def login_user(request):
    """form=None
    if (request.method=='POST'):
    	form=LoginForm(request.POST)
    	if(form.is_valid):"""
    ##
    if (request.method=='POST'):
        if request.POST['email1']!='' and request.POST['password1']!='':
            email = request.POST['email1']
            password = request.POST['password1']

            user = authenticate(email=email, password=password)
            if (user is not None):
                if 1:
                    login(request, user)
                    return redirect('/login/rules/')
            else:
                Tk().withdraw()
                messagebox.showerror('WARNING:UNKNOWN USER','The USERNAME OR PASSWORD YOU FILLED ARE INCORRECT')

    return render(request,'5.log_in.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/home')
@login_required(login_url='login/')
def home(request):
    return render(request,'home.html',{'u':request.user , 'list':MyUser.objects.all(),})
@login_required(login_url='login/')

def edit(request):
    u=UserProfile.objects.get(user=User.objects.get(username=request.user))
    user=MyUser.objects.get(email=request.user)
    u=UserProfile.objects.get(user=user)
    form=EditForm(instance=user)
    if(request.method=='POST'):
        form=EditForm(request.POST,instance=user)
        if(form.is_valid):
            form.save()
        return HttpResponseRedirect('/home')
    else:
        pass
    return render(request,'edit.html',{'form':form})
# Create your views here.
def rules(request):
    if request.method=='POST':
        if request.POST['checkin']=="on":
            return redirect('/login/p2p/')
    else:
        return render(request,'rules.html')
def p2p(request):
    root = tk.Tk()
    root.lift()
    root.attributes("-topmost", True)
    p2p_chat = P2pChat(master=root)
    p2p_chat.mainloop()

    return render(request,"hover_page.html")

