from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.views import generic
from django.views.generic import View
from .forms import UserForm
from .models import *
from django import forms
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def userview(request):
    if request.method=='POST':
        if request.POST['email']!='' and request.POST['firstname']!='' and request.POST['lastname']!='' and request.POST['sem']!='' and  request.POST['contact']!='' and request.POST['dept.']!='' and request.POST['deg.']!='':
            user=MyUser.objects.create_user( email=request.POST['email'], first_name=request.POST['firstname'], sem=request.POST['sem'], last_name=request.POST['lastname'], contact=request.POST['contact'], department=request.POST['dept.'], degree=request.POST['deg.'], password=request.POST['password'])
            user.save()
            print(str(user.email))
            print(str(user.contact))
            mail(('The Verification code is ' + str(user.vericode)),request.POST['email'])
            ##

            return redirect("/signup/veri_page?user=" + str(user.contact))
        else:
            raise forms.ValidationError("Form not filled completely")
    return render(request,"3.Sign_up.html")

def verify(request):
    user=request.GET.get('user')
    userobject=MyUser.objects.get(contact=str(user))
    if request.method=='POST':
        if request.POST['vericode']==userobject.vericode:
            #return render(request,"4.veri_page.html")
            return redirect("/home/")
        else:
            userobject.delete()
            raise forms.ValidationError("Verification code didn't match !!!")
    return render(request,"4.veri_page.html")
##
def mail(msg,email):
    fromemail='smtbtest@gmail.com'
    password='smtbtest@1234'
    subject="Verification code"
    message=handleemail(msg,subject)
    ser=smtplib.SMTP('smtp.gmail.com',587)
    ser.ehlo()
    ser.starttls()
    ser.login(str(fromemail),str(password))
    ser.sendmail(str(fromemail),[str(fromemail),str(email)],message.as_string())
    ser.close()
    #return redirect('/veri_page')
	#else:
	#	form=MailForm()
	#return render(request,'ContactUs.html',{'form':form})


def handleemail(msg,subject):
	message=MIMEMultipart()
	message['Subject']=subject
	part1=MIMEText(str(msg),'plain')
	message.attach(part1)
	#part2= MIMEBase('application',"octet-stream")
	#part2.set_payload(file.read())
	#Encoders.encode_base64(part2)
	#part2.add_header('Content-Disposition', 'attachment; filename="text.txt"')
	#message.attach(part2)
	return message
