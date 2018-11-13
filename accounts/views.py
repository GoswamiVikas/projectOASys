from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from accounts.forms import (
							RegisterationForm,
							EditProfileForm,
							StudentProfileForm,
						)
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
	return render(request, 'accounts/home.html')

def register(request):
	if request.method == 'POST':
		form = RegisterationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/accounts/profile')
		else:
			return render(request,'accounts/register.html')
	else:
		form = RegisterationForm()
		args = {'form':form}
		return render(request, 'accounts/register.html', args)

@login_required
def view_profile(request):
	args = {'user': request.user}
	return render(request, 'accounts/view_profile.html', args)

@login_required
def edit_profile(request):
	if request.method == 'POST':
		form = StudentProfileForm(request.POST, instance=request.user)

		if  form.is_valid():
			form.save()
			return redirect('/accounts/profile')

	else:
		form = StudentProfileForm(instance=request.user)
		args = {'form': form, 'user':request.user}
		return render(request, 'accounts/edit_profile.html', args)

@login_required
def change_password(request):
	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save
			update_session_auth_hash(request,form.user)
			return redirect('/accounts/profile')
		else:
			return redirect('/accounts/change_password')

	else:
		form = PasswordChangeForm(user=request.user)
		args = {'form': form}
		return render(request, 'accounts/change_password.html', args)



















