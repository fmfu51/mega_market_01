from django.http import HttpRequest, HttpResponse


# Create your views here.
def create_question(request: HttpRequest):
    return HttpResponse("안녕")