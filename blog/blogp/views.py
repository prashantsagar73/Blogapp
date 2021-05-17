from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import post
from django.contrib.auth.models import User
# Create your views here.

def home(request):
    context = {
        'posts': post.objects.all()
    }
    return render(request,"blog/home.html",context)

# for listing the post to get their id 
class PostListView(ListView):
    model = post 
    template_name = "blog/home.html"  #<app>/<model> _ <viewtype>.html
    context_object_name = 'posts'
    ordering =['-date_time']
    paginate_by = 9

class PostDetailView(DetailView):
    model = post
    template_name = 'blog/post_detail.html' 

class PostCreateView(LoginRequiredMixin, CreateView):
    model = post
    fields =['title','content']
    template_name = 'blog/post_forms.html' 


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = post
    fields =['title','content']    
    template_name = 'blog/post_forms.html' 


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False       
   
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = post
    template_name = 'blog/post_confirm_delete.html' 
    success_url= "/"  

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False  


class UserPostListView(ListView):
    model = post 
    template_name = "blog/user_posts.html"  #<app>/<model> _ <viewtype>.html
    context_object_name = 'posts'
    ordering =['-date_time']
    paginate_by = 4

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date_time')

def about(request):
    return render(request,"blog/about.html")