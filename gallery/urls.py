from django.urls import path

from gallery.views import PictureListView, PictureDetailView, PictureAddView, UpdatePictureView, DeletePictureView

urlpatterns = [
    path('', PictureListView.as_view(), name='index'),
    path('pictures/<int:pk>/', PictureDetailView.as_view(), name="picture_detailed"),
    path('pictures/add/', PictureAddView.as_view(), name="picture_add"),
    path('pictures/<int:pk>/update/', UpdatePictureView.as_view(), name="picture_update"),
    path('pictures/<int:pk>/delete/', DeletePictureView.as_view(), name='picture_delete'),
    path('pictures/<int:pk>/confirm-delete/', DeletePictureView.as_view(), name='picture_confirm_delete'),
]
