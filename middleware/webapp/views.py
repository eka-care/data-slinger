from django.http import HttpResponse

# from .auth import Auth


def index(request):
    return HttpResponse("Hello, world!")
