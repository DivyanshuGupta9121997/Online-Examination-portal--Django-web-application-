from django import forms
from customauth.models import MyUser
from django.utils.translation import ugettext_lazy as _

class MailForm(forms.Form):
	from_email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("FROM :"))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password :"))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password (again) :"))
	to_email = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("TO :"))
	subject=forms.CharField(widget=forms.TextInput(attrs=dict(required=False,max_length=20)), label=_("SUBJECT :"))
	message=forms.CharField(widget=forms.Textarea)
	file=forms.FileField()
	def clean(self):
		#raise forms.ValidationError(_("The two password fields did not match."))
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("The two password fields did not match."))
		return self.cleaned_data
	