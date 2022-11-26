from django.shortcuts import render
from django.views.generic import ListView

from gallery.models import Picture


# Create your views here.
class PictureListView(ListView):
    template_name = "picture/index.html"
    model = Picture
    context_object_name = "pictures"