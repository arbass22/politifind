from django.shortcuts import render
from politifind.models import Bill
import unidecode

def bills(request):
    bills = Bill.objects.all()

    return render(
        request,
        'bills.html',
        context={'bills': bills},
    )
