"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.principal, name="Home"),
    path('about/', views.about, name="about"),
    path('blog/', views.blog, name="blog"),
    path('contact/', views.contact, name="contact"),
    path('detail/', views.detail, name="detail"),
    path('feature/', views.feature, name="feature"),
    path('quote/', views.quote, name="quote"),
    path('policy/', views.policy, name="policie"),
    path('service/', views.service, name="service"),
    path('team/', views.team, name="team"),
    path('dashboard/', views.dashboard_with_pivot, name='dashboard_with_pivot'),
    path('data', views.pivot_data, name='pivot_data'),
    path('confirm/<str:email>/<str:conf_num>/', views.confirm, name='confirm'),
    path('success/<str:email>/', views.success, name='success'),
    path('testimonial/', views.testimonial, name="testimonial"),
    path('set_cookie/', views.set_cookie, name='set_cookie'),
    path('set_cookie/', views.view, name='set_cookie'),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    
]
