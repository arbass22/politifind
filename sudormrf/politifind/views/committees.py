from django.shortcuts import render
from politifind.models import Committee

def committees(request):
    committees = Committee.objects.all()
    page = {
        "tabs": [{
            "name": "Members",
            "url": "#",
            },
            {
            "name": "Bills",
            "url": "#",
            }],
        "active_tab": "Members"
    }

    return render(
        request,
        'committees.html',
        context={"committees":committees, "page":page},
    )
