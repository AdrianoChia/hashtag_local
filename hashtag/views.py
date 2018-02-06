from django.shortcuts import render
from django.utils import timezone
from .models import Status

def status(request):
    status = Status.objects.all()
    return render(request, 'hashtag/status.html', {'status': status})
