from django.shortcuts import render, get_object_or_404, redirect
from .forms import TodoForm
from .models import Todo


# Create your views here.
def todos(request):
    todos = Todo.objects.all()
    return render(request, "index.html", {"todos": todos})


def todo_details(request, id):
    todo = get_object_or_404(Todo, pk=id)
    return render(request, "todo_details.html", {"todo": todo})


def add_todo(request):
    if request.method == "POST":
        print("Form submitted")
        form = TodoForm(request.POST, request.FILES)
        print(f"POST data: {request.POST}")
        print(f"FILES data: {request.FILES}")
        if form.is_valid():
            print("Form is valid")
            todo = form.save()
            print(f"Todo saved with id: {todo.id}")
            return redirect("todos")  # Make sure this matches your URL name
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = TodoForm()
    return render(request, "add_todo.html", {"form": form})