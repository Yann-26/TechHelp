from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Banner, Navbar, Topbar, contactUs
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .models import Comment, TeamMembers
from django.http import HttpResponse
import datetime



# def set_cookie(request):
#     response = redirect('home')
#     if request.method == 'POST':
#         cookie_name = request.POST.get('cookie_name')
#         cookie_value = request.POST.get('cookie_value')

#         if cookie_name and cookie_value:
#             max_age = 30 * 24 * 60 * 60  # 30 days in seconds
#             expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age), '%a, %d-%b-%Y %H:%M:%S GMT')
#             response.set_cookie(cookie_name, cookie_value, max_age=max_age, expires=expires, domain=None, secure=False)

#     return response
def view(request):
    response = HttpResponse("hello")
    set_cookie(response, 'name', 'jujule')
    return response


def set_cookie(response, key, value, days_expire=7):
    if days_expire is None:
        max_age = 365 * 24 * 60 * 60  # one year
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(
        datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
        "%a, %d-%b-%Y %H:%M:%S GMT",
    )
    response.set_cookie(
        key,
        value,
        max_age=max_age,
        expires=expires,
        domain=settings.SESSION_COOKIE_DOMAIN,
        secure=settings.SESSION_COOKIE_SECURE or None,
    )



def detail(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        comment = request.POST.get('comment', '')
        parent_id = request.POST.get('parent_id', None)
        commentaire = Comment()
        commentaire.nom = name
        commentaire.email = email
        commentaire.commenter = comment
        if parent_id:
            commentaire.parent_comment = Comment.objects.get(id=parent_id)

        commentaire.save()
    commentaires = Comment.objects.all()
    datas = {
        'commentaires': commentaires,
    }
    return render(request, 'principal/detail.html', datas)




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


def team(request):
    teams = TeamMembers.objects.filter()
    datas = {
        'teams': teams
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



#QuerySet pour récupérer tous les commentaires actifs des parents pour ce post

