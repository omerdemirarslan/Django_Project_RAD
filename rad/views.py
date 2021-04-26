import requests
import logging

from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect


logger = logging.getLogger(__name__)


def get_home_page(request):
    """
    This Function Renders The Home Page When First Entering The Web Site
    :param request:
    :return:
    """
    return render(request, "pages/home.html", {})
