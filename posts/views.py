"""Posts Views"""

#Django
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

#Form
from posts.forms import PostForm

#Models
from posts.models import Post

class PostsDetailView(LoginRequiredMixin, DetailView):
    """Return post detail"""
    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'


class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all publisehd  post view"""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    paginate_by = 30
    context_object_name = 'posts'

class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post"""
    template_name ='posts/new.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context"""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context