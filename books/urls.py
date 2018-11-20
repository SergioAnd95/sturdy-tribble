from django.urls import path

from . import views

urlpatterns = [
    # path('', views.BooksListView.as_view(), name='list'),
    path('create/', views.BookCreateView.as_view(), name='create'),
    path('edit/<int:pk>/', views.BookEditView.as_view(), name='edit')
]
