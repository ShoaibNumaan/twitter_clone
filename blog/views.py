from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Shoaib',
        'title': 'BP 1',
        'content': "First post in jhool",
        'date_posted': 'October 26, 2021'
    },
    {
        'author': 'Numaan',
        'title': 'BP 2',
        'content': "Second post in jhool",
        'date_posted': 'October 27, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', { 'title': 'About'})