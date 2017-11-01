from django.shortcuts import render
from politifind.models import Committee

def committee(request, cid):
    committee = Committee.objects.get(cid=cid)
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
        'committees_members.html',
        context={"committee":committee, "page":page},
    )
