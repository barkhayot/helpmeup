from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from . models import NOTE
from . forms import NoteCreateForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



@login_required(login_url='loginUser')
def allNotes(request):
    note  = NOTE.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(note, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = NoteCreateForm()
    if request.method == 'POST':
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('allNotes')
    
    context = {
        'notes': note,
        'form': form,
        'page_obj': page_obj
    }
    return render(request, 'note/allNote.html', context)


@login_required(login_url='loginUser')
def createNote(request):
    form = NoteCreateForm()
    if request.method == 'POST':
        form = NoteCreateForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('allNotes')
    
    context = {
        'form': form
    }
    return render(request, 'note/createNote.html', context)

@login_required(login_url='loginUser')
def noteDetail(request, pk):
    note    = get_object_or_404(NOTE, pk=pk)
    context = {
        'note': note
    }
    return render(request, 'note/noteDetail.html', context)


@login_required(login_url='loginUser')
def noteDelete(request, pk):
    note  = get_object_or_404(NOTE, pk=pk)
    if request.method == 'POST':
        note.delete()
        return redirect('allNotes')
    context ={
        'note': note
    }

    return render(request, 'note/noteDelete.html', context) 