from django.shortcuts import render
from .models import Contact, Banner, Navbar, Topbar, contactUs



def base(request):
    
    banner = Banner.objects.filter(status=True)
    navbar = Navbar.objects.filter(status=True)
    topbar = Topbar.objects.filter(status=True)
    datas = {
        'banner': banner,
        'navbar': navbar,
        'topbar': topbar,
    }
    return render(request, 'bases/base.html', datas)




def principal(request):
    
    datas = {

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



def contact(request) :
    if request.method == 'POST' : 
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
    
    return render(request, 'principal/contact.html')