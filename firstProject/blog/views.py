from django.http import HttpResponse


def home(request):
    return HttpResponse("<h1>I'm home Page</h1>")


def about(request):
    return HttpResponse("<h1>I'm About Page</h1>")
