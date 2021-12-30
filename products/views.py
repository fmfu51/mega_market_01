from django.http import HttpRequest, HttpResponse


def product_list(request: HttpRequest):
    return HttpResponse("안녕")