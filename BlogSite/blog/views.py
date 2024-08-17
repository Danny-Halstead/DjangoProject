from django.shortcuts import render

posts = [
    {
        'author': 'Danny',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 16, 2024',
    },
{
        'author': 'John Wayne',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 17, 2024',
    },
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')