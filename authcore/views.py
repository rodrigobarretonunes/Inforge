from django.shortcuts import render
from django.http import request


def manage_users_view(request):
    return render(request, 'authcore/manage_users.html')
