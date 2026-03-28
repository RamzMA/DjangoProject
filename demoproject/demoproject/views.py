from django.http import HttpResponse

def handler404(request, exception):
    return HttpResponse("Error: Not found 404")

