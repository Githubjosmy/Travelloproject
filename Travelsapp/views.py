from django.shortcuts import render
from .models import places


def index(request):

    dest1 = places.objects.all()
    return render(request,"index.html",{'dest1':dest1})