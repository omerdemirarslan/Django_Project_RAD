import logging

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect


logger = logging.getLogger(__name__)


@csrf_exempt
@login_required
def create_new_developer_user(request):
    """
    This Function Add The New Record Developer User In The Developer Users Model
    :param request:
    :return:
    """
