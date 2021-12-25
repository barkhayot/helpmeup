from django.shortcuts import render, redirect
from . models import testCHART_DATA, testCHART
from . forms import TestCHART_DATAForm, TestCHARTForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator






# """ For Testing Methods """
@login_required(login_url='loginUser')
def all_charts_view(request):
    chart = testCHART.objects.filter(user=request.user).order_by('-created_at')
    paginator = Paginator(chart, 9)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    form = TestCHARTForm()
    if request.method == 'POST':
        form = TestCHARTForm(request.POST)
        if form.is_valid():
            chart = form.save(commit=False)
            chart.user = request.user
            chart.save()
            return redirect('chart_detail_view', pk=chart.pk)
    context = {
        'charts':chart,
        'form': form,
        'page_obj': page_obj
    }
    return render(request, 'tracker/all_chart_view.html', context)

@login_required(login_url='loginUser')
def chart_detail_view(request, pk):
    # calling exact model from db
    chartObj = get_object_or_404(testCHART, pk=pk, user=request.user)

    #  adding data to charts view form
    chart_data = testCHART_DATA.objects.filter(chart=chartObj, user=request.user).order_by('-created_at')
    form = TestCHART_DATAForm()
    if request.method == 'POST':
        form = TestCHART_DATAForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.chart = chartObj
            data.user = request.user
            data.save()
            return redirect('chart_detail_view', pk=chartObj.pk)
    
    context = {
        'chart': chartObj,
        'form': form,
        'chart_datas':chart_data
    }

    return render(request, 'tracker/chart_detail_view.html', context)


# Chart Create view
@login_required(login_url='loginUser')
def chart_create_view(request):
    form = TestCHARTForm()
    if request.method == 'POST':
        form = TestCHARTForm(request.POST)
        if form.is_valid():
            chart = form.save(commit=False)
            chart.user = request.user
            chart.save()
            return redirect('chart_detail_view', pk=chart.pk)
    
    context = {
        'form':form
    } 
    return render(request, 'tracker/chart_create_view.html', context)


@login_required(login_url='loginUser')
def chart_delete(request, pk):
    chart = get_object_or_404(testCHART, pk=pk)
    if request.method == 'POST':
        chart.delete()
        return redirect('all_chart_view')
    context = {
        'chart': chart
    }

    return render(request, 'tracker/chart_delete.html', context)

@login_required(login_url='loginUser')
def chart_data_delete(request, pk):
    #chart = testCHART_DATA.get(id)
    chart_data = get_object_or_404(testCHART_DATA, pk=pk)
    if request.method == 'POST':
        chart_data.delete()
        return redirect('chart_detail_view', pk=chart_data.chart.id)
    context = {
        'chart_data': chart_data
    }
    return render(request, 'tracker/chart_data_delete.html', context)




