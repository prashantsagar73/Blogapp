from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView

from .import views

urlpatterns= [
     path('', PostListView.as_view(), name ="Blog_home"),
     path('user/<str:username>', UserPostListView.as_view(), name ="user-posts"),
     path('post/<int:pk>/', PostDetailView.as_view(), name ="post_detail"),
     path('post/<int:pk>/update/', PostUpdateView.as_view(), name ="post-update"),
     path('post/<int:pk>/delete/', PostDeleteView.as_view(), name ="post-delete"),
     path('post/new/', PostCreateView.as_view(), name ="post-create"),
     path('about/', views.about,name ="Blog_about")
]