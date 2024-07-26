from django.urls import path
from . import views
from .views import HomeView ,PostDetailView ,AddPostView ,UpdatePostView ,DeletePostView
from .views import AddCategoryView ,  LikeView ,SearchResultsView 

urlpatterns = [
   #path('', views.home, name='home'),
   path('' , HomeView.as_view(), name='home' ),
   path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
   path('add_post/', AddPostView.as_view(), name='add_post'),
   path('post/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
   path('post/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
   path('post/<int:pk>/comment/', views.AddCommentView.as_view(), name='add_comment'),
   path('add_category/', views.AddCategoryView.as_view(), name='add_category'),
   path('like/<int:pk>', LikeView, name='like_post'),
   path('search/', SearchResultsView.as_view(), name='search_posts'),
  
]

