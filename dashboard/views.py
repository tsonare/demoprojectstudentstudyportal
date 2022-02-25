from django.shortcuts import render, redirect
from .models import Note
from .forms import *
from django.contrib import messages
from django.views.generic import DetailView

# Create your views here.


def home_authenticated(request):
    return render(request, 'dashboard/home_authenticated.html')


def home_not_authenticated(request):
    return render(request, 'dashboard/home_not_authenticated.html')


def notes(request):
    if request.method == "POST":
        form = Notesform(request.POST)
        if form.is_valid():
            notes = Note(user=request.user,title=request.POST['title'],description=request.POST['description'])
            notes.save()
        messages.success(request, f"Note saved from {request.user.username} successfully.")
        return redirect('notes')
    else:
        form = Notesform()
    notes = Note.objects.filter(user=request.user)
    context = {'notes': notes,'form': form}
    return render(request, 'dashboard/notes.html', context)


def delete_note(request,pk=None):
    Note.objects.get(id=pk).delete()
    messages.success(request, f"Note Deleted from {request.user.username} successfully.")
    return redirect('notes')


class NotesDetailView(DetailView):
    model = Note
    template_name = 'dashboard/notes_detail.html'


def edit_note(request,pk):
    note = Note.objects.get(id=pk)
    form = Notesform(instance=note)
    if request.method == "POST":
        form = Notesform(request.POST, instance=note)
        if form.is_valid():
            form.save()
        messages.success(request, f"Updated Note saved from {request.user.username} successfully.")
        return redirect('notes')
    context = {'form':form,}
    return render(request, 'dashboard/edit_note.html', context)


