from django.shortcuts import render
from django.urls import reverse
from politifind.models import Committee

def committee(request, cid, page=None):
    committee = Committee.objects.get(cid=cid)
    page_context = {
        "tabs": [{
            "name": "Members",
            "url": reverse('committee', args=[committee.cid]),
            },
            {
            "name": "Bills",
            "url": reverse('committee', args=[committee.cid, "bills"]),
            }],
        "active_tab": "Members"
    }

    if page == "members":
        page_context["active_tab"] = "Members"
        return render(
            request,
            'committees_members.html',
            context={"committee":committee, "page":page_context},
        )
    elif page == "bills":
        page_context["active_tab"] = "Bills"
        return render(
            request,
            'committees_bills.html',
            context={"committee":committee, "page":page_context},
        )
    else:
        return render(
            request,
            'committees_members.html',
            context={"committee":committee, "page":page_context},
        )
