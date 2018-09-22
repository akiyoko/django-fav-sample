from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView

from .forms import FavoriteForm
from .models import Favorite


class ListFavoriteView(ListView):
    model = Favorite


class CreateFavoriteView(LoginRequiredMixin, CreateView):
    form_class = FavoriteForm
    success_url = reverse_lazy('fav:index')
    template_name = 'fav/favorite_form.html'

    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)


class UpdateFavoriteView(LoginRequiredMixin, UpdateView):
    model = Favorite
    form_class = FavoriteForm
    success_url = reverse_lazy('fav:index')
    template_name = 'fav/favorite_form.html'
