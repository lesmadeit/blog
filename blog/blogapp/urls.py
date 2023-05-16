from django.urls import re_path, include
from .views import Index, DetailArticleView

urlpatterns = [
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^$', Index.as_view(), name='index'),
    re_path('<int:pk>', DetailArticleView.as_view(), name='detail_article'),
    
]