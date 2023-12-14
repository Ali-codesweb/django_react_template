from django.http import JsonResponse
from django.http import HttpRequest


def dummy_view(request: HttpRequest):
    return JsonResponse({"asdad": "Asdasd"})
