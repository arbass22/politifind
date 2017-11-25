from random import randrange
from django.shortcuts import render
from politifind.models import Bill, BillCommittee, BillAction, PoliticianVote

def bill(request, bid):
    bill = Bill.objects.get(bid=bid)
    all_bills = Bill.objects.all()
    bill_committees = BillCommittee.objects.filter(bill=bill)
    if len(bill_committees) == 0:
        similar_bills = []
    else:
        i = randrange(0, len(bill_committees))
        similar_bills = map(lambda bc: bc.bill, BillCommittee.objects.filter(committee=bill_committees[i].committee))[:3]
    bill_actions = BillAction.objects.filter(bill=bill)
    yay = bill.total_yes
    nay = bill.total_no

    votes = {
        'users': {
            'total': 100,
            'total_yes': 70,
            'total_no': 30
        }
    }

    if yay+nay > 0:
        votes['congress'] = {
            'total': yay+nay,
            'total_yes': yay,
            'total_no': nay
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
