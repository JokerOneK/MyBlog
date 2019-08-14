from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, AccessMixin
from django.views import generic
from django.urls import reverse_lazy

from .models import Post


class IndexView(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'Blog/index.html'
    context_object_name = 'latest_post_list'


class DetailView(generic.DetailView):

    template_name = "Blog/detail_post.html"
    queryset = Post.objects.all()


class AboutView(generic.TemplateView):
    template_name = 'Blog/about.html'


class CreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    template_name = 'Blog/create_post.html'
    fields = ['theme',
              'post_text',
              ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateView(LoginRequiredMixin, UserPassesTestMixin, AccessMixin, generic.UpdateView):
    model = Post
    fields = ['theme',
              'post_text',
              ]
    template_name = 'Blog/update_post.html'
    success_url = reverse_lazy('Blog:index')

    def handle_no_permission(self):
        return redirect('Blog:error')

    def test_func(self):
        return self.get_object().author == self.request.user


class DeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView, AccessMixin):
    model = Post
    template_name = 'Blog/delete_post.html'
    success_url = reverse_lazy('Blog:index')

    def handle_no_permission(self):
        return redirect('Blog:error')

    def test_func(self):
        return self.get_object().author == self.request.user


class ErrorView(generic.TemplateView):
    template_name = 'Blog/post_error.html'



