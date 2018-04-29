# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import smtplib

from django.shortcuts import render
from django.shortcuts import redirect
from signup.models import *
#from email.MIMEMultipart import MIMEMultipart
#from email.MIMEBase import MIMEBase
#from email import Encoders
#from email.mime.text import MIMEText
# Create your views here.
new=1
def mail(request):
	form =None
	if (request.method=='POST'): #-----------
			fromemail=shivamxarora@gmail.com
			password=1234@abc
			toemail=Myuser.objects.get(email=email)
			subject="Verification code"#form.cleaned_data['subject']
			#file=request.FILES['file']
			#msg=form.cleaned_data['message']
			message=handleemail(msg,subject)
			ser=smtplib.SMTP('smtp.gmail.com',587)
			ser.ehlo()
			ser.starttls()
			ser.login(str(fromemail),str(password))
			ser.sendmail(str(fromemail),[str(fromemail),str(toemail)],message.as_string())
			ser.close()
			#return redirect('/veri_page')
	else:
		form=MailForm()
	#return render(request,'ContactUs.html',{'form':form})


def handleemail(msg,subject):
	message=MIMEMultipart()
	message['Subject']=subject
	msg=Myuser.objects.get(vericode)
	part1=MIMEText(str(msg),'plain')
	message.attach(part1)
	#part2= MIMEBase('application',"octet-stream")
	#part2.set_payload(file.read())
	#Encoders.encode_base64(part2)
	#part2.add_header('Content-Disposition', 'attachment; filename="text.txt"')
	#message.attach(part2)
	return message    


