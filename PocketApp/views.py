from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def time(request):
    return render(request, 'time/time.html')

def calc(request):
    return render(request, 'calculator/gpa_calc.html')

def handle_not_found(request, exception):
    return render(request, 'not_found_handler.html', status=404)


