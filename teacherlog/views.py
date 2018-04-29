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
from signup.models import MyUser
from .models import *

#import p2p_chat.classes.client as client
#import p2p_chat.classes.server as server
#from p2p_chat.p2p_chat_ import *

@csrf_protect
def login_user(request):
    """form=None
    if (request.method=='POST'):
    	form=LoginForm(request.POST)
    	if(form.is_valid):"""
    ##
    if (request.method=='POST'):
        if request.POST['name']!='' and request.POST['password']!='':
            email = request.POST['name']
            password = request.POST['password']

            user = authenticate(email=email, password=password)
            if (user is not None):
                if 1:
                    login(request, user)
                    return redirect('/teacherlogin/teacherdetail/')
            else:
                Tk().withdraw()
                messagebox.showerror('WARNING:UNKNOWN USER','The USERNAME OR PASSWORD YOU FILLED ARE INCORRECT')

    return render(request,'teacher_log.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/home')
@login_required(login_url='teacherlogin/')
def home(request):
    return render(request,'home.html',{'u':request.user , 'list':MyUser.objects.all(),})
@login_required(login_url='teacherlogin/')

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
def gques(request):
    root = tk.Tk()
    p2p_chat = P2pChat(master=root)
    p2p_chat.mainloop()
def teacherdetail(request):
    return render(request,"Teacher_login_Exam_Details.html")
