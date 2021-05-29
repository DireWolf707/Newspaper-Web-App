from django.urls import path
from .views import HomeView,ArticleListView,ArticalDetailView,ArticalUpdateView,ArticleCreateView,ArticleDeleteView

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('articles/',ArticleListView.as_view(),name='article_list'),
    path('article/new/',ArticleCreateView.as_view(),name='article_create'),
    path('article/<int:pk>/',ArticalDetailView.as_view(),name='article_detail'),
    path('article/<int:pk>/edit',ArticalUpdateView.as_view(),name='article_update'),
    path('article/<int:pk>/delete',ArticleDeleteView.as_view(),name='article_delete'),
]
