from random import randrange
from django.shortcuts import render
from politifind.models import Bill, BillCommittee, BillAction, PoliticianVote

def bill(request, bid):
    bill = Bill.objects.get(bid=bid)
    all_bills = Bill.objects.all()
    i = randrange(0, len(all_bills))
    similar_bills = all_bills[i:i+3]
    bill_committees = BillCommittee.objects.filter(bill=bill)
    bill_actions = BillAction.objects.filter(bill=bill)
    yay = bill.total_yes
    nay = bill.total_no

    votes = {
        'congress': {
            'total': yay+nay,
            'total_yes': yay,
            'total_no': nay
        },
        'users': {
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
