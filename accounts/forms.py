from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from cuser.forms import AuthenticationForm, UserCreationForm
from OASys import settings
from cuser.models import CUser
from accounts.models import StudentProfile
from django.forms import ModelForm

class RegisterationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = CUser
		fields = (
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
		)
	def save(self, commit=True):
		
		# if RegisterationForm.is_valid(self):
		user = super(RegisterationForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

class EditProfileForm(UserChangeForm):

	class Meta:
		model = CUser
		fields = (
			'email',
			'first_name',
			'last_name',
		)

class StudentProfileForm(ModelForm):
	class Meta:
		model = StudentProfile
		fields = ['course','semester','rollno']