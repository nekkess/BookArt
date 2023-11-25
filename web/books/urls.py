from django.urls import path

from . import views

app_name = "books"

urlpatterns = [
    path('', view=views.index, name='index'),
    path('search/', views.search_view, name='search_view'),
]
