from django.shortcuts import render, redirect
from django.views.generic import ListView,View
from django.views.generic.edit import CreateView ,UpdateView
# Create your views here.
from .models import Todo


class HomePageView(ListView):
    model = Todo
    template_name = "index.html"

    


class AddTodoView(CreateView):
    model = Todo
    # template_name = "index.html"
    fields = ["title","description","priority"]
    success_url = "/"


    
class UpdateToDo(UpdateView):
    model = Todo
    # template_name = "index.html"
    fields = "__all__"
    success_url = "/"

class DoneToDo(View):
    
    def get(self,request,todo_id):
        todo = Todo.objects.get(id=todo_id)
        todo.doned = True
        todo.save()
        return redirect("/")