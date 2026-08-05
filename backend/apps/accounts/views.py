from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.http import url_has_allowed_host_and_scheme

from .forms import ProfileUpdateForm, RegisterForm


def register_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            messages.success(
                request,
                "Your account has been created successfully.",
            )

            return redirect("dashboard")

    else:

        form = RegisterForm()

    return render(
        request,
        "accounts/register.html",
        {
            "form": form,
        },
    )


def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    next_url = request.GET.get("next", "").strip()

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:

            login(request, user)

            if (
                next_url
                and url_has_allowed_host_and_scheme(
                    next_url,
                    allowed_hosts={request.get_host()},
                    require_https=request.is_secure(),
                )
            ):
                return redirect(next_url)

            return redirect("dashboard")

        messages.error(
            request,
            "Invalid username or password.",
        )

    return render(
        request,
        "accounts/login.html",
    )


@login_required
def change_password_view(request):

    if request.method == "POST":

        form = PasswordChangeForm(
            user=request.user,
            data=request.POST,
        )

        if form.is_valid():

            user = form.save()

            update_session_auth_hash(
                request,
                user,
            )

            messages.success(
                request,
                "Your password has been changed successfully.",
            )

            return redirect("accounts:profile")

    else:

        form = PasswordChangeForm(
            user=request.user,
        )

    return render(
        request,
        "accounts/password_change.html",
        {
            "form": form,
        },
    )


@login_required
def profile_view(request):

    context = {
        "profile_user": request.user,
    }

    return render(
        request,
        "accounts/profile.html",
        context,
    )


@login_required
def profile_edit_view(request):

    if request.method == "POST":

        form = ProfileUpdateForm(
            request.POST,
            request.FILES,
            instance=request.user,
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                "Your profile has been updated successfully.",
            )

            return redirect("accounts:profile")

    else:

        form = ProfileUpdateForm(
            instance=request.user,
        )

    return render(
        request,
        "accounts/profile_edit.html",
        {
            "form": form,
        },
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        "You have been logged out successfully.",
    )

    return redirect("home")


# ============================================================
# FORGOT PASSWORD / PASSWORD RESET
# ============================================================


def password_reset_request_view(request):

    password_reset_view = auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset.html",
        email_template_name="accounts/password_reset_email.html",
        subject_template_name="accounts/password_reset_subject.txt",
        success_url=reverse_lazy(
            "accounts:password_reset_done"
        ),
    )

    return password_reset_view(request)


def password_reset_done_view(request):

    password_reset_done_view = auth_views.PasswordResetDoneView.as_view(
        template_name="accounts/password_reset_done.html",
    )

    return password_reset_done_view(request)


def password_reset_confirm_view(request, uidb64, token):

    password_reset_confirm_view = (
        auth_views.PasswordResetConfirmView.as_view(
            template_name="accounts/password_reset_confirm.html",
            success_url=reverse_lazy(
                "accounts:password_reset_complete"
            ),
        )
    )

    return password_reset_confirm_view(
        request,
        uidb64=uidb64,
        token=token,
    )


def password_reset_complete_view(request):

    password_reset_complete_view = (
        auth_views.PasswordResetCompleteView.as_view(
            template_name="accounts/password_reset_complete.html",
        )
    )

    return password_reset_complete_view(request)