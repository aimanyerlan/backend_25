from django.shortcuts import render, get_object_or_404, redirect
from .models import Note
from .forms import NoteForm
# Create your views here.
def notes_list(request):
    notes = Note.objects.all()
    return render(request, 'note/notes_list.html', {'notes': notes})

def note_detail(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, 'note/note_detail.html', {'note': note})

def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes_list')
    else:
        form = NoteForm()
    return render(request, 'note/note_form.html', {'form': form})

def note_edit(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_detail', id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, 'note/note_form.html', {'form': form})

def note_delete(request, id):
    note = get_object_or_404(Note, id=id)
    note.delete()
    return redirect('notes_list')