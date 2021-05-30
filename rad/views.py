import logging

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout

from .helper.forms import RegistrationForm, LoginForm
from .helper.general_helper import create_new_user
from .helper.messages import *

logger = logging.getLogger(__name__)


@cache_page(60 * 15)
def get_login_page(request):
    """
    This Function Renders The Login Page and Login Form
    :param request:
    :return:
    """
    login_form = LoginForm()

    return render(request, "forms/login.html", {
        "login_form": login_form
    })


@csrf_exempt
def get_register_page(request):
    """
    This Function Render Registration Page and Registration Form
    :param request:
    :return:
    """
    register_form = RegistrationForm()

    return render(request, "forms/registration.html", {
        "register_form": register_form
    })


@csrf_exempt
def get_home_page(request):
    """
    This Function Renders The Home Page When First Entering The Web Site
    :param request:
    :return:
    """
    return render(request, "pages/home.html", {})


@require_http_methods(["POST"])
@csrf_exempt
def create_new_developer_user(request):
    """
    This Function Create The New Record Developer User In The Developer Users Model
    :param request:
    :return:
    """
    register_form = RegistrationForm(request.POST)

    if register_form.is_valid():
        first_name = register_form.cleaned_data["first_name"]
        last_name = register_form.cleaned_data["last_name"]
        mail_address = register_form.cleaned_data["mail_address"]
        password = register_form.cleaned_data["password"]
        confirm_password = register_form.cleaned_data["confirm_password"]
        github_address = register_form.cleaned_data["github_address"]
        linkedin_address = register_form.cleaned_data["linkedin_address"]
        twitter_address = register_form.cleaned_data["twitter_address"]

        new_user = create_new_user(
            first_name=first_name,
            last_name=last_name,
            mail_address=mail_address,
            password=password,
            confirm_password=confirm_password,
            github_address=github_address,
            linkedin_address=linkedin_address,
            twitter_address=twitter_address
        )

        if new_user:
            return redirect("login-page")
        else:
            messages.warning(request, PASSWORD_CONFIRM_PASSWORD_NOT_SAME)

            return redirect("registration-form")
    else:
        register_form = RegistrationForm()

    return redirect("registration-form", {
        "register_form": register_form
    })


@require_http_methods(["POST"])
@csrf_exempt
def get_login(request):
    """
    This Function Controls User Login Authenticate
    :param request:
    :return:
    """
    login_form = LoginForm(request.POST)

    if login_form.is_valid():
        user_name = login_form.cleaned_data["user_name"]
        password = login_form.cleaned_data["password"]

        user = authenticate(request,
                            username=user_name,
                            password=password
                            )

        if user is not None:
            if user.is_active:
                login(request, user)

                return redirect("home")
            else:
                messages.warning(request, INVALID_USER_LOGIN)

                return redirect("registration-form")
        else:
            messages.error(request, WRONG_USER_OR_PASSWORD)

            return redirect("registration-form")
    else:
        messages.warning(request, WRONG_USER_OR_PASSWORD)

        return redirect("login-page")
