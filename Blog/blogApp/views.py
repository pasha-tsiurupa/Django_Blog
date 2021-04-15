from django.shortcuts import render

posts = [
    {
        'author': 'Paul',
        'title': 'Blog Post1',
        'date_posted': 'April 15, 2021',
        'content': 'First post content'
    },
    {
        'author': 'Ili',
        'title': 'Blog Post2',
        'content': 'Second post content',
        'date_posted': 'April 16, 2021'
    }
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blogApp/home.html', context)


def about(request):
    return render(request, 'blogApp/about.html', {'title': 'About'})
