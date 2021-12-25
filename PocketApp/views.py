from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def handle_not_found(request, exception):
    return render(request, 'not_found_handler.html', status=404)


