from django.urls import path

from gallery.views import PictureListView

urlpatterns = [
    path('', PictureListView.as_view(), name='index'),
]
