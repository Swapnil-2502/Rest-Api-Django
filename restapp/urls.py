from django.urls import path
from .views import Employee_list

urlpatterns = [
    path('employeelist/',Employee_list),
    # path('employeelist/<int:id>/',Employee_list),
]
