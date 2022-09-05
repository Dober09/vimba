from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('home/',views.article_page,name='new_home'),
    path('<slug:slug>',views.article_detail,name='detail')
]