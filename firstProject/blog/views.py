from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        "author": "Umair",
        "title": "Blog Post 1",
        "content": "First Post By Umair (NizzyPedia)",
        "data_posted": "Feburary 22nd, 2024",
    },
    {
        "author": "Khan",
        "title": "Blog Post 2",
        "content": "Second Post By Khan (NizzyPedia)",
        "data_posted": "Feburary 31st, 2024",
    },
]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
