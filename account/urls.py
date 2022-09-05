from django.urls import path
from . import views
# a
urlpatterns = [
    path('login/', views.login_page, name="login"),
    path('logout/', views.logout_page, name="logout"),
    path('signup/', views.signup_page, name="signup"),
]