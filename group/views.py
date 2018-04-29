from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from login.views import *
from group.urls import *

def homepage(request):
    return render(request,"1.Index_Page.html")
def signlog(request):
    return render(request,"2.sign_log.html")
def signup(request):
    return render(request,"3.Sign_up.html")
def veripage(request):
    return render(request,"4.veri_page.html")
def login(request):
    return render(request,"5.log_in.html")
def about(request):
    return render(request,"About.html")
def contact(request):
    return render(request,"contact.html")
def rules(request):
    return render(request,"rules.html")
def teacherlog(request):
    return render(request,"teacher_log.html")
def teacherdetail(request):
    return render(request,"Teacher_login_Exam_Details.html")
