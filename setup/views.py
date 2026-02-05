from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello Work")

def about(request):
    return HttpResponse("About me")