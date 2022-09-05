from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('home',views.article_page,name='home'),
    path('<str:slug>',views.article_detail,name='detail')
]