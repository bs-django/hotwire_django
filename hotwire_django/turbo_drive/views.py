from django.shortcuts import render, redirect
from hotwire_django.tasks.forms import TaskForm


def create_view(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = TaskForm()
    return render(request, 'turbo_drive/create.html', {'form': form})

