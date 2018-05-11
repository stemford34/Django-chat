from django.shortcuts import render
from django.http import HttpResponseRedirect

from registration.models import UserInfo
from .models import DialogUsers, DialogMassage, DialogInfo


def main_page(request):
    return render(request, "chat/index.html")