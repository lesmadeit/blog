from django.urls import re_path, path, include
from .views import Index, DetailArticleView, LikeArticle, Featured, DeleteArticle

urlpatterns = [
    re_path(r'^tinymce/', include('tinymce.urls')),
    re_path(r'^$', Index.as_view(), name='index'),
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    re_path(r'^featured/$', Featured.as_view(), name='featured'),
    path('<int:pk>/delete', DeleteArticle.as_view(), name='delete_article')
]