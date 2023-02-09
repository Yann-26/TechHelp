from authentification.models import Profile
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from authentification.models import *
import uuid
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib.auth import get_user_model
from authentification.forms import UserUpdateForm


# Create your views here.


def home(request):
    return render(request , 'principal/index.html')

def edit_profile(request):           
    datas = {
        
    }
    return render(request, 'edit_profile.html', datas)


def login_or_register(request):  
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        action = request.POST.get('action')
        print(action)
             # connexion
        if action == "login":
            user_obj = User.objects.filter(username = username).first()
            if user_obj is None:
                messages.success(request, 'User not found.')
                return redirect('login_or_register')

            profile_obj = Profile.objects.filter(user = user_obj ).first()
            if not profile_obj.is_verified:
                messages.success(request, 'Profile is not verified check your mail.')
                return redirect('login_or_register')
            user = authenticate(username = username , password = password)
            if user is None:
                messages.success(request, 'Wrong password.')
                return redirect('login_or_register')
            login(request , user)
            return redirect('/')
            #### creation de compte
        elif action == "register":
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password_confirm = request.POST.get('password_confirm')
            if password != password_confirm:
                messages.success(request, 'Passwords do not match.')
                return redirect('login_or_register')
            try:
                if User.objects.filter(username=username).first():
                    messages.success(request, 'Username is taken.')
                    return redirect('login_or_register')
                if User.objects.filter(email=email).first():
                    messages.success(request, 'Email is taken.')
                    return redirect('login_or_register')
                user_obj = User(
                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user_obj.set_password(password)
                user_obj.save()
                auth_token = str(uuid.uuid4())
                profile_obj = Profile.objects.create(
                    user=user_obj,
                    auth_token=auth_token
                )
                profile_obj.save()
                send_mail_after_registration(email, auth_token)
                return redirect('/token')
            except Exception as e:
                print(e)
    return render(request, 'login_or_register.html')


def success(request):
    return render(request , 'success.html')


def token_send(request):
    return render(request , 'token_send.html')

def signout(request):
    logout(request)
    messages.success(request, 'logout successfully!')
    return redirect('Home')

##### 
def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()
    

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login_or_register')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('login_or_register')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'error.html')


def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )
    


# #############PASSWORS RESET
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password_reset.html", context={"password_reset_form":password_reset_form})



def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'{user_form}, Your profile has been updated!')
            return redirect('profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        # form.fields['description'].widget.attrs = {'rows': 1}
        return render(request, 'profile.html', context={'form': form})

    return redirect("Home")




