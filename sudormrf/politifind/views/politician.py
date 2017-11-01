from django.shortcuts import render
from politifind.models import Politician, PoliticianVote, CommitteeMembership, BillSponsorship

def politician(request, pid, page=None):
    politician = Politician.objects.get(pid=pid)
    recent_votes = PoliticianVote.objects.filter(pid__exact=pid)
    committee_membership = CommitteeMembership.objects.filter(pid__exact=pid)
    bill_sponsorship = BillSponsorship.objects.filter(pid__exact=pid)

    context = {
        'politician': politician,
        'committee_membership': committee_membership,
        'bill_sponsorship': bill_sponsorship,
        'recent_votes': recent_votes,
    }

    if page == 'votes':
        return render(
            request,
            'politician_votes.html',
            context=context,
        )
    elif page == 'bills':
        return render(
            request,
            'politician_bills.html',
            context=context,
        )
    else:
        return render(
            request,
            'politician_home.html',
            context=context,
        )
