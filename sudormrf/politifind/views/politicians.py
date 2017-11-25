from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from politifind.models import Politician

def politicians(request):
    politicians_list = Politician.objects.all()
    paginator = Paginator(politicians_list, 25)

    page = request.GET.get('page')
    try:
        politicians = paginator.page(page)
    except PageNotAnInteger:
        politicians = paginator.page(1)
    except EmptyPage:
        politicians = paginator.page(paginator.num_pages)

    return render(
        request,
        'politicians.html',
        context={'politicians': politicians},
    )
