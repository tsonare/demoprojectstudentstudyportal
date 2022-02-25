from django.shortcuts import render, redirect
from .models import Note
from .forms import *
from django.contrib import messages
from django.views.generic import DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView
from django.forms.widgets import HiddenInput
# Create your views here.


def home_authenticated(request):
    return render(request, 'dashboard/home_authenticated.html')


def home_not_authenticated(request):
    return render(request, 'dashboard/home_not_authenticated.html')

# class NoteCreateView(CreateView):
#     template_name = 'dashboard/notes.html'
#     model = Note
#     fields = ['title','description','user']
#     # fields['user'].widget = forms.HiddenInput()
#     success_url = 'notes'
    


# class NotesFormView(FormView):
#     template_name = 'dashboard/notes.html'
#     form_class = NotesForm
#     success_url = 'notes'    
#     def get_initial(self):
#         initial = super(NotesFormView,self).get_initial(NotesForm)
#         return initial
#     def form_valid(self, form):
#         # form.save()      
#         # import pdb;pdb.set_trace()
#         note = form.save(get_initial)
#         # note.user = self.request.user
#         note.save()
#         return super().form_valid(form)


class NotesFormView(FormView):
    form_class = NotesForm
    def get_form(self,form_class):
        form = super(NotesFormView, self).get_form(form_class)
        form.fields['user'].widget = forms.HiddenInput()

    def get_initial(self):
        initial = super(NotesFormView, self).get_initial()
        initial['user'] = self.request.user


class NoteCreateView(NotesFormView,CreateView):
    template_name = 'dashboard/notes.html'
    model = Note
    fields = ['title','description','user']
    # fields['user'].widget = forms.HiddenInput()
    success_url = 'notes'
        
    



# def notes(request):
#     if request.method == "POST":
#         form = NotesForm(request.POST)
#         if form.is_valid():
#             notes = Note(user=request.user,title=request.POST['title'],description=request.POST['description'])
#             notes.save()
#         messages.success(request, f"Note saved from {request.user.username} successfully.")
#         return redirect('notes')
#     else:
#         form = NotesForm
#     notes = Note.objects.filter(user=request.user)
#     context = {'notes': notes,'form': form}
#     return render(request, 'dashboard/notes.html', context)


def delete_note(request,pk=None):
    Note.objects.get(id=pk).delete()
    messages.success(request, f"Note Deleted from {request.user.username} successfully.")
    return redirect('notes')


class NotesDetailView(DetailView):
    model = Note
    template_name = 'dashboard/notes_detail.html'


def edit_note(request,pk):
    note = Note.objects.get(id=pk)
    form = NotesForm(instance=note)
    if request.method == "POST":
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
        messages.success(request, f"Updated Note saved from {request.user.username} successfully.")
        return redirect('notes')
    context = {'form':form,}
    return render(request, 'dashboard/edit_note.html', context)




# https://stackoverflow.com/questions/45128646/django-rest-framework-deny-user-from-push-when-user-is-not-object-owner