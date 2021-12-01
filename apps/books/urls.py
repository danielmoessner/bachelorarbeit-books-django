from django.urls import path
from apps.books import views

urlpatterns = [
    path('', views.BooksView.as_view())
]
