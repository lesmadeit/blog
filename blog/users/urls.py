from django.urls import re_path
from .views import RegisterView

urlpatterns = [
    re_path(r'^register/$', RegisterView.as_view(), name='register' ), 
    
]
