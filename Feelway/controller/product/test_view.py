from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hellow Test View</h1>")