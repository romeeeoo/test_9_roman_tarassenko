from django.urls import path

from accounts.views import LoginView, logout_view, ProfileView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path('account/<int:pk>/', ProfileView.as_view(), name='account'),
]