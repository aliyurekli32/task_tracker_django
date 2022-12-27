from django.urls import path
from .views import (todo_list_create, todo_detail)

urlpatterns = [
        path('list-create',todo_list_create),    
        path('detail/<int:pk>',todo_detail),    
]
