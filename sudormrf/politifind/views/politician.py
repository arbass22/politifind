from django.shortcuts import render
from django.urls import reverse
from politifind.models import Politician, PoliticianVote, CommitteeMembership, BillSponsorship

def politician(request, pid, page=None):
    politician = Politician.objects.get(pid=pid)
    recent_votes = PoliticianVote.objects.filter(pid__exact=pid)[:5]
    committee_membership = map(lambda x: x.cid, CommitteeMembership.objects.filter(pid__exact=pid))
    bill_sponsorship = map(lambda x: x.bid, BillSponsorship.objects.filter(pid__exact=pid))

    page_context = {
        "tabs": [{
            "name": "Home",
            "url": reverse('politician', args=[politician.pid]),
            },
            {
            "name": "Votes",
            "url": reverse('politician', args=[politician.pid, "votes"]),
            },
            {
            "name": "Bills",
            "url": reverse('politician', args=[politician.pid, "bills"]),
            }],
    }

    context = {
        'politician': politician,
        'committee_membership': committee_membership,
        'bill_sponsorship': bill_sponsorship,
        'recent_votes': recent_votes,
        'page': page_context,
    }


    if page == 'votes':
        print "Hello"
        context['page']['active_tab'] = "Votes"
        return render(
            request,
            'politician_votes.html',
            context=context,
        )
    elif page == 'bills':
        context['page']['active_tab'] = "Bills"
        return render(
            request,
            'politician_bills.html',
            context=context,
        )
    else:
        print "Hello2"
        context['page']['active_tab'] = "Home"
        return render(
            request,
            'politician_home.html',
            context=context,
        )
