from random import randrange
from django.shortcuts import render
from politifind.models import Bill, BillCommittee, BillAction, PoliticianVote

def bill(request, bid):
    bill = Bill.objects.get(bid=bid)
    all_bills = Bill.objects.all()
    i = randrange(0, len(all_bills))
    similar_bills = all_bills[i:i+3]
    bill_committees = BillCommittee.objects.filter(bid__exact=bid)
    bill_actions = BillAction.objects.filter(bid__exact=bid)
    votes = PoliticianVote.objects.filter(bid__exact=bid)
    yay = filter(lambda v: v.vote == 'YAY', votes)
    nay = filter(lambda v: v.vote == 'NAY', votes)

    votes = {
        'congress': {
            'date': 'November 15, 2017',
            'total': len(votes),
            'total_yes': len(yay),
            'total_no': len(nay)
        },
        'users': {
            'date': 'November 14, 2017',
            'total': 100,
            'total_yes': 70,
            'total_no': 30
        }
    }

    return render(
        request,
        'bill.html',
        context={
            'bill':bill,
            'bill_actions':bill_actions,
            'bill_committees':bill_committees,
            'similar_bills':similar_bills,
            'votes':votes,
        }
    )
