from django.shortcuts import render,redirect
from django.contrib import messages
from .models import *
import bcrypt
from datetime import datetime

# Create your views here.
def current_user(request):
    return User.objects.get(id=request.session['user_id'])
def index(request):
    return render(request, 'login_reg/index.html')
def new(request):
    return render(request,'login_reg/succes.html')

def login(request):
    if request.method != 'POST':
        return redirect('/')
    else:
        if request.POST.get('email') == '' or request.POST.get('password') == '':
            messages.error(request, 'invalid credentials')
            return redirect('/')
        check = User.objects.loginUser(request.POST)
        if check['status'] == False:
            messages.error(request, check['message'])
            return redirect('/')
        else:
            request.session['user_id'] = check['user'].id
            return redirect('/success')

def createUser(request):
	if request.method != 'POST':
		return redirect('/')
	else:
		check = User.objects.validateUser(request.POST)
		if check[0] == False:
			for error in check[1]:
				messages.error(request, error)
			return redirect('/')
		else:
			#create the user
			hashed_pw = bcrypt.hashpw(request.POST.get('password').encode(), bcrypt.gensalt())
			user = User.objects.create(
				name = request.POST.get('name'),
				email = request.POST.get('email'),
				password = hashed_pw
			)
			request.session['user_id'] = user.id
			return redirect('/success')
def logout(request):
    request.session.clear()
    return redirect('/')
