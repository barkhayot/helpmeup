from django.shortcuts import render, redirect, get_object_or_404
from . models import URL_DATA
from . forms import LinkCreateForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator




@login_required(login_url='loginUser')
def allURL(request):
    link = URL_DATA.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(link, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = LinkCreateForm()
    if request.method == 'POST':
        form = LinkCreateForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            return redirect('allURL')
    
    context = {
        'links': link,
        'form': form,
        'page_obj': page_obj
    } 
    return render(request, 'url/allURL.html', context)

@login_required(login_url='loginUser')
def createURL(request):
    form = LinkCreateForm()
    if request.method == 'POST':
        form = LinkCreateForm(request.POST)
        if form.is_valid():
            link = form.save(commit=False)
            link.user = request.user
            link.save()
            return redirect('allURL')
    context = {
        'form': form
    }
    return render(request, 'url/createURL.html', context)

@login_required(login_url='loginUser')
def URLDetail(request, pk):
    link = get_object_or_404(URL_DATA, pk=pk, user=request.user)
    context = {
        'link': link
    }
    return render(request, 'url/URLDetail.html', context)

@login_required(login_url='loginUser')
def URLDelete(request, pk):
    link = get_object_or_404(URL_DATA, pk=pk, user=request.user)
    if request.method == 'POST':
        link.delete()
        return redirect('allURL')
    context = {
        "link": link
    }
    
    return render(request, 'url/urlDelete.html', context)
