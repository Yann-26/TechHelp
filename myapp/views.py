from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact, Banner, Navbar, Topbar, contactUs, Order
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from .models import Comment, TeamMembers, Reponse_Commentaire, Policy
from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from .forms import SubscriberForm
import random
from django.core.mail import send_mail
from django.urls import reverse
from django.http import JsonResponse
from django.core import serializers



def get_model_statistics():
    # Statistiques pour le modèle Contact
    contact_count = Contact.objects.count()

    # Statistiques pour le modèle Banner
    banner_count = Banner.objects.count()

    # Statistiques pour le modèle Navbar
    navbar_count = Navbar.objects.count()

    # Statistiques pour le modèle Topbar
    topbar_count = Topbar.objects.count()

    # Statistiques pour le modèle contactUs
    contactus_count = contactUs.objects.count()

    # Statistiques pour le modèle Comment
    comment_count = Comment.objects.count()

    # Statistiques pour le modèle Reponse_Commentaire
    reponse_commentaire_count = Reponse_Commentaire.objects.count()

    # Statistiques pour le modèle TeamMembers
    team_members_count = TeamMembers.objects.count()

    # Statistiques pour le modèle Subscriber
    subscriber_count = Subscriber.objects.count()

    # Statistiques pour le modèle Newsletter
    newsletter_count = Newsletter.objects.count()

    # Création d'un dictionnaire avec les statistiques
    statistics = {
        'Contact': contact_count,
        'Banner': banner_count,
        'Navbar': navbar_count,
        'Topbar': topbar_count,
        'contactUs': contactus_count,
        'Comment': comment_count,
        'Reponse_Commentaire': reponse_commentaire_count,
        'TeamMembers': team_members_count,
        'Subscriber': subscriber_count,
        'Newsletter': newsletter_count,
    }

    return statistics



def pivot_data(request):
    dataset = Contact.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)



def dashboard_with_pivot(request):
    return render(request, 'principal/dashboard_with_pivot.html', {})

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
    reponses = None
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        comment = request.POST.get('comment', '')
        response = request.POST.get('reponse_comment', '')
        parent_id = request.POST.get('parent_id', None)
        reponse = Reponse_Commentaire()
        commentaire = Comment()
        reponse.reponse_comment = response
        reponse.nom = name
        reponse.email = email
        commentaire.nom = name
        commentaire.email = email
        commentaire.commenter = comment
        commentaire.save()
        if parent_id:
            Reponse_Commentaire.parent_comment = Reponse_Commentaire.objects.get(id=parent_id)
            reponse.save()
        reponses = Reponse_Commentaire.objects.all()
    commentaires = Comment.objects.prefetch_related('reponses').all()
    datas = {
        'reponses': reponses,
        'commentaires': commentaires,

    }
    return render(request, 'principal/detail.html', datas)



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


def policy(request):
    policies = Policy.objects.filter(status=True)
    datas = {
        'policies': policies
    }
    return render(request, 'principal/policy.html', datas)

def service(request):
    datas = {

    }
    return render(request, 'principal/service.html', datas)



def contact(request):
    if request.method == 'POST':
        nom = request.POST.get('name')
        email = request.POST.get('email')
        sub = request.POST.get('subject')
        com = request.POST.get('commentaire')
            
        contact = Contact()
        contact.nom = nom
        contact.email = email 
        contact.subject = sub 
        contact.commentaire = com 
        contact.save()
            
    return render(request, "principal/contact.html")



# ########################################### NEWSLETTER #################################################

def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)


def principal(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            sub = form.save(commit=False)
            sub.conf_num = random_digits()
            sub.save()
            email_subject = 'Newsletter Confirmation'
            email_body = 'Thank you for signing up for my email newsletter! \
                Please complete the process by \
                <a href="{}"> clicking here to \
                confirm your registration</a>.'.format(
                    request.build_absolute_uri(reverse('confirm', kwargs={'email': sub.email, 'conf_num': sub.conf_num}))
                )
            send_mail(email_subject, email_body, settings.FROM_EMAIL, [sub.email], html_message=email_body)
            return redirect('success', email=sub.email)
    else:
        form = SubscriberForm()

    banners = Banner.objects.filter(status=True)
    navbar = Navbar.objects.filter(status=True)
    topbar = Topbar.objects.filter(status=True)
    datas = {
        'banners': banners,
        'navbar': navbar,
        'topbar': topbar,
        'form': form,
    }

    return render(request, 'principal/index.html', datas)



def success(request, email):
    return render(request, 'bases/base.html', {'email': email, 'action': 'added', 'form': SubscriberForm()})


def confirm(request, email, conf_num):
    email = request.GET.get('email')
    conf_num = request.GET.get('conf_num')
    try:
        sub = Subscriber.objects.get(email=email)
        if sub.conf_num == conf_num:
            sub.confirmed = True
            sub.save()
            return render(request, 'principal/index.html', {'email': sub.email, 'action': 'confirmed'})
        else:
            return render(request, 'principal/index.html', {'email': sub.email, 'action': 'denied'})
    except Subscriber.DoesNotExist:
        return render(request, 'principal/index.html', {'email': email, 'action': 'denied'})



def delete(request, email, conf_num):
    email = request.GET.get('email')
    conf_num = request.GET.get('conf_num')
    try:
        sub = Subscriber.objects.get(email=email)
        if sub.conf_num == conf_num:
            sub.delete()
            return HttpResponseRedirect(reverse('unsubscribed'))
        else:
            return render(request, 'principal/delete_error.html')
    except Subscriber.DoesNotExist:
        return render(request, 'principal/delete_error.html')

