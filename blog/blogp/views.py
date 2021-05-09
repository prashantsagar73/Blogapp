from django.shortcuts import render
from .models import post
# Create your views here.
posts =[
    {
        'author': "prashant sagar",
        'title': 'this is jus testing',
        'content': 'hello how are everything going on?',
    },
    {
        'author': "prashant sagar",
        'title': 'this is jus testing',
        'content': 'hello how are everything going on?',
    }

]


def home(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request,"home.html",context)

def about(request):
    return render(request,"about.html")