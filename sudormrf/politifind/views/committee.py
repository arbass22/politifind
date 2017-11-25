from django.shortcuts import render
from django.urls import reverse
from politifind.models import Committee, CommitteeMembership, BillCommittee, SubCommittee

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
            },
            {
                "name": "Subcommittees",
                "url": reverse('committee', args=[committee.cid, "subcomittees"]),
            }],
        "active_tab": "Members"
    }

    if page == "bills":
        page_context["active_tab"] = "Bills"
        bills = map(lambda bc: bc.bill, BillCommittee.objects.filter(committee_id=cid))
        return render(
            request,
            'committees_bills.html',
            context={"committee":committee, "page":page_context, "bills": bills},
        )
    elif page == "subcomittees":
        page_context["active_tab"] = "Subcommittees"
        subcommittees = SubCommittee.objects.filter(parent=committee)
        return render(
            request,
            'committees_subcommittees.html',
            context={"committee":committee, "page":page_context, "subcommittees":subcommittees},
        )
    else:
        page_context["active_tab"] = "Members"
        members = map(lambda cm: cm.politician, CommitteeMembership.objects.filter(committee=committee))
        return render(
            request,
            'committees_members.html',
            context={"committee":committee, "page":page_context, "members":members},
        )
