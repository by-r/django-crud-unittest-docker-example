from django.urls import path, include
from .views import TodoCreateView, TodoListView, TodoDetailView, TodoDeleteView, TodoUpdateView 
from django.views.generic import RedirectView

urlpatterns = [
    path('todos/', TodoListView.as_view(), name='index' ),
    path('todos/create/', TodoCreateView.as_view(), name='create' ),
    path('todos/<pk>/', TodoDetailView.as_view(), name='detail' ),
    path('todos/<pk>/update/', TodoUpdateView.as_view(), name='update' ),
    path('todos/<pk>/delete/', TodoDeleteView.as_view(), name='delete' ),
    
]