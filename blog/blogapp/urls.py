from django.urls import re_path, include
from .views import Index

urlpatterns = [
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^$', Index.as_view(), name='index'),
    
]