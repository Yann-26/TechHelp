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



@login_required
def profile_information(request, username):
    users = Profile_information.objects.all()
    user = request.user
    profile = Profile_information() 
    if request.method == 'POST':
        city = request.POST.get('city', '')
        country = request.POST.get('country', '') 
        phone_number = request.POST.get('phone_number', '')
        Birthday = request.POST.get('Birthday', '')
        Profession = request.POST.get('Profession', '')
        Bio = request.POST.get('Bio', '')
        profile_photo = request.POST.get('profile_photo', '')
        cover = request.POST.get('cover', '')
        gender = request.POST.get('gender', '')
        Address = request.POST.get('Address', '')
        Rela_status = request.POST.get('Rela_status', '')
        location = request.POST.get('location', '')

        profile.city = city
        profile.country = country
        profile.phone_number = phone_number
        profile.Birthday = Birthday
        profile.Profession = Profession
        profile.Bio = Bio
        profile.profile_photo = profile_photo
        profile.cover = cover
        profile.gender = gender
        profile.Address = Address
        profile.Rela_status = Rela_status
        profile.location = location
        profile.save()
        
    user = get_user_model().objects.filter(username=username).first()
    datas = {
            'users': users
        }
    if user:
        profile = Profile_information()
        return render(request, 'profile.html', datas)

    return redirect("Home")   





