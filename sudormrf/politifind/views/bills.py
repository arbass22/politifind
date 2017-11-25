from django.shortcuts import render
from politifind.models import Bill
import unidecode

def bills(request):
    bills = Bill.objects.all()
    for b in bills:
        b.name = unidecode.unidecode(b.name)

    return render(
        request,
        'bills.html',
        context={'bills': bills},
    )
