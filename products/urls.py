from django.urls import path 
from .views import ListView, BookListView,BookDetailView,BookCreateView,BookDeleteView,AddReviewView,ReviewDeleteView,ReviewUpdateView


app_name = 'products'
urlpatterns = [
    path('books/',BookListView.as_view(),name='book_list'),
    path('deatail/<int:pk>',BookDetailView.as_view(),name='book_detail'),
    path('create/',BookCreateView.as_view(),name='book_create'),
    path('delete/<int:pk>',BookDeleteView.as_view(),name='book_delete'),
    path('add_review/<int:pk>', AddReviewView.as_view(), name='add_review'),  
    path('review_delete/<int:pk>', ReviewDeleteView.as_view(), name='review_delete'),
    path('review_update/<int:pk>', ReviewUpdateView.as_view(), name='review_update'),
]