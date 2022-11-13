from django.template import loader
from django.http import HttpResponse
from .models import Members

def index(request):
    mymembers = Members.objects.all().values()
    output = ""
    for x in mymembers:
        output += x["firstName"]
    return HttpResponse(output)