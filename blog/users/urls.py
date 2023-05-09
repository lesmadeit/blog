from django.urls import re_path
from .views import RegisterView
from django .contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^login/$', auth_views.LoginView.as_view(template_name='users/login.html'), name='login' ),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout' ),
    re_path(r'^register/$', RegisterView.as_view(), name='register' ),
     
    
]
