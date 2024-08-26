from django.urls import path, include
from apiApp import views

urlpatterns = [
    path('get-books/', views.BookViewSet, name='book-list'),
    path('transactions/',views.Transactions.as_view())
]