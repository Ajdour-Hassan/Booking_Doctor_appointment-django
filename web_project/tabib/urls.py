from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

   path('', views.home , name='home'),
   path('login', views.login_user , name='login'),
   path('logout', views.logout_user , name='logout'),
   path('register', views.register , name='register'),
   path('myprofile' , views.myprofile , name='myprofile'),
   path('profile_update' , views.profile_update , name='profile_update'),
   path('<slug:slug>', views.profile , name='profile'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)