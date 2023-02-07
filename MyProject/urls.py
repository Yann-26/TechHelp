from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from graphene_django.views import GraphQLView




urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', include('authentification.urls')),
    path('', include('newsletter.urls')),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),  
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

