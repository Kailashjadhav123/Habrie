from django.urls import path, include
from .views import StudentListCreateView, StudentUpdateView, StudentDeleteView

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:id>/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:id>/delete/', StudentDeleteView.as_view(), name='student-delete'),

]