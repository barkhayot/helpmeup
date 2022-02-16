from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogCreationForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator



# Get Blogs View
@login_required(login_url='loginUser')
def GetBlogs(request):
    blog = Blog.objects.filter(private=False).order_by('-created_at')
    paginator = Paginator(blog, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'blogs': blog,
        'page_obj': page_obj
    }
    return render(request, 'blog/getblogs.html', context)

# Get Private Blogs View
@login_required(login_url='loginUser')
def GetPrivateBlogs(request):
    blog = Blog.objects.filter(user=request.user, private=True).order_by('-created_at')
    paginator = Paginator(blog, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'blogs': blog,
        'page_obj': page_obj
    }
    return render(request, 'blog/getprivateblogs.html', context)

# Create Blog View
@login_required(login_url='loginUser')
def CreateBlog(request):
    form = BlogCreationForm()
    if request.method == 'POST':
        form = BlogCreationForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('getblogs')
    context = {
        'form': form
    }
    return render(request, 'blog/createblog.html', context)


# Blog Detail View
@login_required(login_url='loginUser')
def BlogDetail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    context = {
        'blog': blog
    }
    return render(request, 'blog/blogdetail.html', context)

# Private Blog Detail View
@login_required(login_url='loginUser')
def PrivateBlogDetail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.user != blog.user:
        return redirect('forbidden')
    context = {
        'blog': blog
    }
    return render(request, 'blog/blogdetail.html', context)


# Update Blog View
@login_required(login_url='loginUser')
def UpdateBlog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    form = BlogCreationForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect('getblogs')
    context = {
        'form': form
    }
    return render(request, 'blog/updateblog.html', context)

# User Related Blogs View
@login_required(login_url='loginUser')
def UserBlog(request):
    blog = Blog.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(blog, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'blogs': blog,
        'page_obj': page_obj
    }
    return render(request, 'blog/userblog.html', context)

# Blog Delete View
@login_required(login_url='loginUser')
def BlogDelete(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.user != blog.user:
            return redirect('forbidden')
    if request.method == 'POST':
        blog.delete()
        return redirect('userblog')
    context = {
        'blog': blog
    }
    return render(request, 'blog/blogdelete.html', context)


# Access Not Allowed View
@login_required(login_url='loginUser')
def Forbidden(request):
    return render(request, 'blog/forbidden.html')