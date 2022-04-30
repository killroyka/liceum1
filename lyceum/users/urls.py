from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path

from . import views

urlpatterns = [
    path("users/", views.UserListView.as_view(), name="user_list"),
    path("users/<int:id>/", views.UserDetailView.as_view(), name="user_detail"),
    path("user_list/", views.UserListView.as_view(), name="user_list"),
    path("user_detail/<int:id>/", views.UserDetailView.as_view(), name="user_detail"),
    path("profile/", views.ProfileView.as_view(), name="profile"),

    # аутентификация:
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("passwordchange/", PasswordChangeView.as_view(template_name="users/password_change.html"),
         name="password_change"),
    path("passwordchangedone/", PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
         name="password_changedone"),
    path("password_reset/", PasswordResetView.as_view(template_name="users/password_reset.html"),
         name="password_reset"),
    path("password_reset/done/", PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name="password_resetdone"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(template_name="users/password_reset_сonfirm.html"),
         name="reset"),
    path("reset/done/", PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name="reset_done"),
]
