from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from users.models import User

def index(request):
    users = User.objects.all().values()
    users = list(users)
    return JsonResponse({
        'details': 'List of all users.',
        'users': users
    }, safe=False)

def create_user(request):
    return JsonResponse({
        'details': 'Create a new user.'
    })


# Create your views here.
