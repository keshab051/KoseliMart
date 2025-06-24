from django.http import HttpResponse

def Homepage(request):
    return HttpResponse("hello")