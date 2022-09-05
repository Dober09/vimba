from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Displaying all date to be read
    path('missing_people/', views.missing_people, name='missing_people'),
    path('wanted_people/', views.wanted_people, name='wanted_people'),
    # selected persons
    path('person_of_intrest/<str:pk>', views.person_of_intrest, name='POI'),
    path('missing_person/<str:pk>', views.missing_pep, name='missing_person'),
    # create
    path('adding_missing_person', views.add_missing_person,
         name="adding_missing_person"),
    path('adding_wanted_person', views.add_wanted_person,
         name="adding_wanted_person"),
    # update
    path('updating_missing_person/<str:pk>/',
         views.update_missing, name="update_missing"),
    path('updating_wanted_person/<str:pk>/',
         views.update_wanted, name="update_wanted"),
    # delete
    path('remove_wanted_person/<str:pk>/',
         views.remove_wanted, name="remove_wanted"),
    path('remove_missing_person/<str:pk>/',
         views.remove_missing, name="remove_missing"),
    # login
    
]
