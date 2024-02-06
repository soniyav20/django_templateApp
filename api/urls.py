from django.urls import path
from . import views
from .views import EmployeeCreateAPIView,EmployeeDeleteAPIView,EmployeeListAPIView,EmployeeUpdateAPIView

urlpatterns = [
    path('getemp/', EmployeeListAPIView.as_view()),
    path('update/<int:EmpId>/', EmployeeUpdateAPIView.as_view()),
    path('delete/<int:EmpId>/', EmployeeDeleteAPIView.as_view()),
    path('create/', EmployeeCreateAPIView.as_view()),
]
