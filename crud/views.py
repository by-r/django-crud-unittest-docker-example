from django.shortcuts import render
from django.views.generic import View, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Todolist

# Create your views here.
class TodolisBaseView(View):
    model = Todolist
    context_object_name = 'todos'
    fields = '__all__'
    success_url = reverse_lazy('index')
    
class TodoCreateView(TodolisBaseView, CreateView):
    """Create Function

    Args:
        TodolisBaseView (_type_): _description_
        CreateView (_type_): _description_
    """
    
class TodoListView(TodolisBaseView, ListView):
    """List Function

    Args:
        TodolisBaseView (_type_): _description_
        ListView (_type_): _description_
    """
    
class TodoDetailView(TodolisBaseView, DetailView):
    """Detail Function

    Args:
        DetailView (_type_): _description_
    """
    
class TodoUpdateView(TodolisBaseView, UpdateView):
    """Update Function

    Args:
        TodolisBaseView (_type_): _description_
        UpdateView (_type_): _description_
    """
    
class TodoDeleteView(TodolisBaseView, DeleteView):
    """Delete Function

    Args:
        TodolisBaseView (_type_): _description_
        DeleteView (_type_): _description_
    """