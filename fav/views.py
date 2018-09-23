from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from .forms import FavoriteForm
from .models import Favorite


class ListFavoriteView(ListView):
    model = Favorite


# class CreateFavoriteView(LoginRequiredMixin, CreateView):
#     form_class = FavoriteForm
#     success_url = reverse_lazy('fav:index')
#     template_name = 'fav/favorite_form.html'
#
#     def form_valid(self, form):
#         form.instance.submitter = self.request.user
#         # super().form_valid() の中で form が save() される
#         return super().form_valid(form)

class CreateFavoriteView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        context = {'form': FavoriteForm()}
        return render(request, 'fav/favorite_form.html', context)

    def post(self, request, *args, **kwargs):
        form = FavoriteForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, 'fav/favorite_form.html', {'form': form})

        favorite = form.save(commit=False)
        favorite.submitter = self.request.user
        favorite.save()
        return redirect(reverse('fav:index'))


class UpdateFavoriteView(LoginRequiredMixin, UpdateView):
    model = Favorite
    form_class = FavoriteForm
    success_url = reverse_lazy('fav:index')
    template_name = 'fav/favorite_form.html'
