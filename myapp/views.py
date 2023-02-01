from django.shortcuts import render, redirect
from .models import Contact, Banner, Navbar, Topbar, contactUs
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.conf import settings



def principal(request):
    banners = Banner.objects.filter(status=True)
    navbar = Navbar.objects.filter(status=True)
    topbar = Topbar.objects.filter(status=True)
    datas = {
        'banners': banners,
        'navbar': navbar,
        'topbar': topbar,
    }

    return render(request, 'principal/index.html', datas)


def about(request):
    
    datas = {

    }
    return render(request, 'principal/about.html', datas)


def blog(request):
    datas = {

    }
    return render(request, 'principal/blog.html', datas)


def detail(request):
    datas = {

    }
    return render(request, 'principal/detail.html', datas)


def team(request):
    datas = {

    }
    return render(request, 'principal/team.html', datas)


def testimonial(request):
    datas = {

    }
    return render(request, 'principal/testimonial.html', datas)


def quote(request):
    datas = {

    }
    return render(request, 'principal/quote.html', datas)
    

def feature(request):
    datas = {

    }
    return render(request, 'principal/feature.html', datas)



def service(request):
    datas = {

    }
    return render(request, 'principal/service.html', datas)



def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        com = request.POST.get('message')
            
        contact = Contact()
        contact.nom = nom
        contact.email = email 
        contact.subject = sub 
        contact.commentaire = com 
        contact.save()
            
        subject = "Merci pour votre message"
        message = "Nous vous répondrons dans un délai de 24 heures."
        email_from = settings.EMAIL_HOST_USER
        recipient_list = email
        send_mail(subject, message, email_from, [recipient_list])
        return render(request, 'principal/success.html')
    return render(request, "principal/contact.html")
