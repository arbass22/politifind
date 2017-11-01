from django.shortcuts import render
from django.urls import reverse
from politifind.models import Committee, CommitteeMembership, BillCommittee

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

    if page == "bills":
        page_context["active_tab"] = "Bills"
        bills = map(lambda x: x.bid, BillCommittee.objects.filter(cid__exact=cid))
        return render(
            request,
            'committees_bills.html',
            context={"committee":committee, "page":page_context, "bills": bills},
        )
    else:
        page_context["active_tab"] = "Members"
        members = map(lambda x: x.pid, CommitteeMembership.objects.filter(cid__exact=cid))
        return render(
            request,
            'committees_members.html',
            context={"committee":committee, "page":page_context, "members":members},
        )
