from django.urls import path
from . import views

urlpatterns = [
    path('list_category/<slug:category_slug>/', views.list_categories, name='list_category'),
]

