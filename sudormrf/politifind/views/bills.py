from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from politifind.models import Bill

def bills(request):
    bills_list = Bill.objects.all()
    paginator = Paginator(bills_list, 25)

    page = request.GET.get('page')
    try:
        bills = paginator.page(page)
    except PageNotAnInteger:
        bills = paginator.page(1)
    except EmptyPage:
        bills = paginator.page(paginator.num_pages)

    return render(
        request,
        'bills.html',
        context={'bills': bills},
    )
