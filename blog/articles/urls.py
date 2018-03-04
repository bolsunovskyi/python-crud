from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListCreate.as_view()),
    path('categories/<int:pk>/', views.CategoryDetail.as_view()),
    path('', views.ArticleListCreate.as_view()),
    path('<int:pk>/', views.ArticleDetail.as_view()),
]
