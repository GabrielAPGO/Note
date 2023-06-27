from django.shortcuts import render, get_object_or_404
from .models import Notes

from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import NotesForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def notes(request):
    notes = Notes.objects.filter(user=request.user).order_by("importance").reverse()
    return render(request, 'notes.html', {'notes': notes})

def new_note(request):
    if request.method == 'POST':
        form = NotesForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()

            messages.success(request, 'The note was created successfully.')
            return HttpResponseRedirect(reverse('notes'))
        
    form = NotesForm()
    return render(request, 'new_note.html', {"form": form})

def note(request, id):
    note = Notes.objects.get(id=id)
    return render(request, 'note.html', {'note': note})

def note_update(request, id):
    note = get_object_or_404(Notes, id=id)
    form = NotesForm(request.POST or None, request.FILES or None, instance=note)
    if form.is_valid():
        form.save()
        
        messages.success(request, 'The note has been successfully updated.')
        return HttpResponseRedirect(reverse('note', args=[note.id]))
         
    return render(request, 'note_update.html', {"form": form})

def note_delete(request, id): 
    note = Notes.objects.get(id=id)
    if request.method == 'POST':         
        note.delete()
        messages.success(request, 'The note has been successfully deleted.')
        return HttpResponseRedirect(reverse('notes'))
    return render(request, 'note_delete.html')
