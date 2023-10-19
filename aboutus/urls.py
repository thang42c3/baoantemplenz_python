from django.urls import path
from . import views

urlpatterns = [
    path('<slug:en_slug>/', views.single_aboutus_post, name='single_aboutus_post'),
]

