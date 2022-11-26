from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import redirect
from django.views.generic import TemplateView, DetailView

from accounts.forms import LoginForm


# Create your views here.

class LoginView(TemplateView):
    template_name = "login.html"
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {"form": form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            return redirect("index")
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        if not user:
            return redirect("login")
        login(request, user)
        return redirect("index")


def logout_view(request):
    logout(request)
    return redirect("index")


class ProfileView(DetailView):
    model = get_user_model()
    template_name = "user_detail.html"
    context_object_name = "user_obj"

    def get_context_data(self, **kwargs):
        favorite_pictures = self.object.favorite_pictures.all()
        print(favorite_pictures)
        kwargs["favorite_pictures"] = favorite_pictures
        return super().get_context_data(**kwargs)

    # def post(self, request, *args, **kwargs):
    #     account_id = request.POST.get("cust_id")
    #     account = Account.objects.get(pk=account_id)
    #     user = request.user
    #     account.subscriptions.add(user)
    #     return redirect('index')


