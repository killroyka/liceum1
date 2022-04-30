from django.shortcuts import redirect

from .models import User
from django.shortcuts import get_object_or_404
from .forms import UserForm, BirthdayForm, RegisterForm
from django.contrib.auth import login
from raitng.models import Raiting
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = RegisterForm

    def form_valid(self, form, **kwargs):
        new_user = form.save()
        login(self.request, new_user)
        return redirect("profile")


class ProfileView(LoginRequiredMixin, FormView):
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        user_form = UserForm(self.request.POST or None,
                             initial={"email": self.request.user.email, "first_name": self.request.user.first_name,
                                      "last_name": self.request.user.last_name})
        birthday_form = BirthdayForm(self.request.POST or None,
                                     initial={"birthday": self.request.user.birthday.birthday})
        raitings_of_favorite_items = Raiting.objects.prefetch_related("user").prefetch_related("item"). \
            filter(star="5").filter(user_id=self.request.user.id)

        return {"user_form": user_form, "birthday_form": birthday_form,
                "raitings_of_favorite_items": raitings_of_favorite_items}

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if 'name' in request.POST or 'email' in request.POST:
            user_form = UserForm(request.POST)

            if user_form.is_valid():
                request.user.email = user_form.cleaned_data["email"]
                request.user.first_name = user_form.cleaned_data["first_name"]
                request.user.last_name = user_form.cleaned_data["last_name"]
                request.user.save(update_fields=["email", "first_name", "last_name"])
                return redirect("profile")

        if 'birthday' in request.POST:
            birthday_form = BirthdayForm(request.POST)

            if birthday_form.is_valid():
                request.user.birthday.birthday = birthday_form.cleaned_data["birthday"]
                request.user.birthday.save(update_fields=["birthday"])
                request.user.save(update_fields=["email", "first_name", "last_name"])
                return redirect("profile")

        return redirect('profile')


class UserListView(TemplateView):
    template_name = "users/user_list.html"

    def get_context_data(self, **kwargs):
        users = User.objects.all().prefetch_related("birthday").only("username", "birthday")
        context = {"users": users}
        return context


class UserDetailView(TemplateView):
    template_name = "users/user_detail.html"

    def get_context_data(self, **kwargs):
        id = self.kwargs['id']
        user = get_object_or_404(User, pk=id)
        raitings_of_favorite_items = Raiting.objects.prefetch_related("user").prefetch_related("item"). \
            filter(star="5").filter(user_id=id)
        context = {"user": user, "raitings_of_favorite_items": raitings_of_favorite_items}
        return context
