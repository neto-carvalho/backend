from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

# Create your views here.


def todo_list_old(request):
    nome = "Rodrigo"
    alunos = ["1. Ana", "2. José", "3. Bia"]
    return render(
        request, "todos/todo_list.html", {"nome": nome, "lista_alunos": alunos}
    )


def todo_list_old(request):
    nome = 'Rodrigo'
    alunos = ['1. Ana', '2. José', '3. Bia']
    return render(request, "todos/todo_list.html", {"nome": nome, "lista_alunos": alunos})

def todo_list(request):
    todos_lista = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": todos_lista})


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
    model = Todo
    fields = ["tittle", "deadline"]
    sucess_url = reverse_lazy("todo list")
    

