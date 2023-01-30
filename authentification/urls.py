from django.urls import path
from authentification import views

urlpatterns = [
    
    path('signup', views.signup, name='signup'),
    # path('signin', views.signin, name='signin'),
    # path('signout', views.signout, name='signout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    # path("password_reset", views.password_reset_request, name="password_reset"),
    
    
]