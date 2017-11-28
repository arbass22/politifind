from django.shortcuts import render
from django.urls import reverse
from politifind.models import Committee, Profile, CommitteeMembership, BillCommittee
from politifind.models import SubCommittee, UserCommitteeSubscription

def committee(request, cid, page=None):
    committee = Committee.objects.get(cid=cid)
    is_subscribed = False
    if request.user.is_authenticated:    
        user = Profile.objects.filter(user=request.user)[0]
        if len(UserCommitteeSubscription.objects.filter(committee=committee, user=user)) > 0:
            is_subscribed = True
    
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
            context={"committee":committee, "page":page_context, "bills": bills, "is_subscribed": is_subscribed},
        )
    elif page == "subcomittees":
        page_context["active_tab"] = "Subcommittees"
        subcommittees = SubCommittee.objects.filter(parent=committee)
        return render(
            request,
            'committees_subcommittees.html',
            context={"committee":committee, "page":page_context, "subcommittees":subcommittees, "is_subscribed": is_subscribed},
        )
    else:
        page_context["active_tab"] = "Members"
        members = map(lambda cm: cm.politician, CommitteeMembership.objects.filter(committee=committee))
        return render(
            request,
            'committees_members.html',
            context={"committee":committee, "page":page_context, "members":members, "is_subscribed": is_subscribed},
        )
