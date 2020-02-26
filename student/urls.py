from django.urls import path
from .views import StudentListView, StudentCreateView, StudentDetailView, StudentUpdateView,StudentDeleteView


urlpatterns = [
    path('', StudentListView.as_view(), name='list'),
    path('add/', StudentCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', StudentDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', StudentUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', StudentDeleteView.as_view(), name='delete'),
]