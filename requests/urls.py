from django.urls import path

from . import views

urlpatterns = [
    path('', views.LatestRequestsListView.as_view(), name='list')
]
