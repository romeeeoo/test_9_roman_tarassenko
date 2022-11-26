from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from gallery.forms import PictureForm
from gallery.models import Picture


# Create your views here.
class PictureListView(ListView):
    template_name = "picture/index.html"
    model = Picture
    context_object_name = "pictures"


class PictureDetailView(DetailView):
    template_name = "picture/detailed.html"
    model = Picture
    context_object_name = 'picture'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        picture = self.get_object()
        picture_favored_by = picture.favored_by.all()
        print(picture_favored_by)
        context["picture_favored_by"] = picture_favored_by
        return super().get_context_data(**context)


class PictureAddView(LoginRequiredMixin, CreateView):
    template_name = "picture/add.html"
    model = Picture
    form_class = PictureForm

    def post(self, request, *args, **kwargs):
        form = self.get_form_class()(request.POST, request.FILES)
        if form.is_valid():
            author = request.user
            image = form.cleaned_data.get('image')
            description = form.cleaned_data.get('description')
            Picture.objects.create(author=author, image=image, description=description)
            return redirect('index')


class UpdatePictureView(UserPassesTestMixin, UpdateView):
    model = Picture
    template_name = "picture/update.html"
    form_class = PictureForm

    def get_success_url(self):
        return reverse("index")

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('gallery.change_picture')


class DeletePictureView(UserPassesTestMixin, DeleteView):
    template_name = 'picture/delete.html'
    model = Picture
    success_url = reverse_lazy('index')

    def test_func(self):
        return self.get_object().author == self.request.user or self.request.user.has_perm('gallery.delete_picture')


