from django.urls import path, include
from .views import list_paciente, create_paciente, update_paciente, delete_paciente

urlpatterns = [
    path('', list_paciente, name='list_paciente'),
    path('<int:id>/', update_paciente, name='update_paciente'),
    path('delete/<int:id>/', delete_paciente, name='delete_paciente'),
    path('new/', create_paciente, name='create_paciente'),
]