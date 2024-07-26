from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView ,CreateView ,UpdateView ,DeleteView 
from .models import Post ,Category , Comment
from .forms import PostForm , EditForm, CommentForm 
from django.urls import reverse_lazy , reverse

#def index(request):
#   return render(request, 'home.html', {})

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
       post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

class HomeView(ListView):
    model = Post
    template_name ='home.html'
    context_object_name = 'all_post'         
    ordering = ['-post_date']          # This is for ordering our post according to date , and - show new post first

    def get_queryset(self):
        queryset = Post.objects.order_by('-post_date')
        return queryset
    
    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = Category.objects.all()
        context["posts_with_likes"] = [(post, post.total_likes()) for post in self.get_queryset() ]
        return context
    
    def get_queryset(self):
        return Post.objects.all().prefetch_related('comments')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["cat_menu"] = Category.objects.all()
        context["total_likes"] = total_likes
        context["liked"] = stuff.likes.filter(id=self.request.user.id).exists()
        context['comment_form'] = CommentForm()
        context['recent_posts'] = Post.objects.order_by('-post_date')[:5]
        return context

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.kwargs['pk']})

class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class SearchResultsView(ListView):
    model = Post
    template_name = 'search_results.html'
    context_object_name = 'all_post'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(title__icontains=query)






