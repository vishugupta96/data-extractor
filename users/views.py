from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='main:login')
def homepage(request):
  return render(request, "home.html",{})

def register(request):
	if request.user.is_authenticated:
		return redirect('main:homepage')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
    

			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('main:login')
			

		context = {'form':form}
		return render(request, 'register.html', context)



def loginUser(request):
	if request.user.is_authenticated:
		return redirect('app:house')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('app:house')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)




def logoutUser(request):
	logout(request)
	return redirect('main:login')

