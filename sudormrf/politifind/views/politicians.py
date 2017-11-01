from django.shortcuts import render
from politifind.models import Politician

def politicians(request):
    politicians = Politician.objects.all()

    return render(
        request,
        'politicians.html',
        context={'politicians': politicians},
    )
