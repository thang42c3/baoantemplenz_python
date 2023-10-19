from django.urls import path
from . import views

urlpatterns = [
    path('<slug:category_slug>/', views.action, name='action'),
    path('<slug:category_slug>/<slug:en_slug>/', views.single_post, name='single_post'),
]

