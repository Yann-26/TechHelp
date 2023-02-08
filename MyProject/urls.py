from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from rest_framework import routers, serializers, viewsets
from django.contrib.auth.models import User
from myapp.models import *

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'nom', 'email', 'commenter', 'parent_comment']
# ViewSets define the view behavior.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Comment', CommentViewSet)


urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('', include('myapp.urls')),
    path('', include('authentification.urls')),
    path('', include('newsletter.urls')),
    path('monapi', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url('', include('social.apps.django_app.urls', namespace='social')),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),  
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

