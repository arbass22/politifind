from django.shortcuts import render
from politifind.models import Bill

def bills(request):
    bills = Bill.objects.all()

    return render(
        request,
        'bills.html',
        context={'bills': bills},
    )
