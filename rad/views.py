import logging

from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login, logout

from .helper.forms import RegistrationForm
from .helper.general_helper import create_new_user
from .helper.messages import PASSWORD_CONFIRM_PASSWORD_NOT_SAME

logger = logging.getLogger(__name__)


def get_login_page(request):
    """
    This Function Renders The Login Page and Login Form
    :param request:
    :return:
    """
    return render(request, "forms/login.html", {})


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


def get_home_page(request):
    """
    This Function Renders The Home Page When First Entering The Web Site
    :param request:
    :return:
    """
    return render(request, "pages/home.html", {})


@require_http_methods(["POST"])
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
