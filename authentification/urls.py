from django.urls import path
from .views import *

urlpatterns = [

    path('' ,  home  , name="home"),
    path('register' , login_or_register , name="login_or_register"),
    path('token' , token_send , name="token_send"),
    path('success' , success , name='success'),
    path('verify/<auth_token>' , verify , name="verify"),
    path('error' , error_page , name="error"),
    path('signout', signout, name='signout'),
    path('profile/<username>', profile_information, name='profile'),
    path("password_reset", password_reset_request, name="password_reset"),
    
]
