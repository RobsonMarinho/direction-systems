from django.shortcuts import render, redirect
from .models import Paciente
from .forms import PacienteForms


def list_paciente(request):
    pacientes = {'list_paciente': Paciente.objects.all()}
    return render(request, "pacientes.html", pacientes)

def video(request):
    videos = {'video': Item.objects.all()}
    return render(request, "video.html", videos)


def create_paciente(request):
    form = PacienteForms(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('list_paciente')

    return render(request, 'pacientes-form.html', {'form': form})

def update_paciente(request, id):
    pacientes = Paciente.objects.get(id=id)
    form = PacienteForms(request.POST or None, instance=pacientes)

    if form.is_valid():
        form.save()
        return redirect('list_paciente')

    return render(request, 'pacientes-form.html', {'form': form, 'pacientes': pacientes})

def delete_paciente(request, id):
    pacientes = Paciente.objects.get(id=id)
    pacientes.delete()
    return redirect('list_paciente')