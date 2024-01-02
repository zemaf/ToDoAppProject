from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from datetime import datetime


def index(request):
    form = TaskForm()
    # vérifier la méthode HTTP
    if request.method == "POST":
        # instancier le formulaire avec les données
        form = TaskForm(request.POST)
        # tester la validité du formulaire
        if form.is_valid():
            # enregister les données
            form.save()
            # rediriger vers l'URL "index"
            return redirect("index")
    tasks = Task.objects.all()
    return render(request, "index.html", context={"tasks": tasks, "task_form": form})


def update_task(request, task_pk):
    task = Task.objects.get(pk=task_pk)  # on peut aussi écrire ...get(id=task_pk)
    form = TaskForm(instance=task)  # on passe l'instance de la tâche à modifier dans le formulaire
    if request.method == "POST":
        # request.POST retourne les données entrée par l'utilisateur et on affecte ces données à l'instance souhaitée
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")
    return render(request, "update_task.html", context={"edit_task_form": form})


C = 0
def delete_task(request, task_pk):
    global C
    C += 1
    print(f"nb d'appels : {C}")
    task = Task.objects.get(pk=task_pk)
    if request.method == "POST":
        task.delete()
        print(f"tâche effacée à {datetime.now()} ")
        return redirect("index")
    print(f"pas de post pour le moment à {datetime.now()}")
    return render(request, "delete_task.html", context={"task": task})


