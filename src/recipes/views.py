from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RecipeForm


class RecipeCreateView(LoginRequiredMixin, CreateView):
    form_class = RecipeForm
    template_name = 'recipes/recipe_create.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(RecipeCreateView, self).form_valid(form)
