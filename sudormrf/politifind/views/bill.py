from random import randrange
from django.shortcuts import render
from politifind.models import Bill, BillCommittee, BillAction, PoliticianVote, UserVote, Profile
from politifind.models import Bill, BillCommittee, BillAction, PoliticianVote, UserBillSubscription, Profile, UserVote

def bill(request, bid):

    bill = Bill.objects.get(bid=bid)
    all_bills = Bill.objects.all()
    bill_committees = BillCommittee.objects.filter(bill=bill)
    is_subscribed = False
    if request.user.is_authenticated:    
        user = Profile.objects.filter(user=request.user)[0]
        if len(UserBillSubscription.objects.filter(bill=bill, user=user)) > 0:
            is_subscribed = True
    if len(bill_committees) == 0:
        similar_bills = []
    else:
        i = randrange(0, len(bill_committees))
        similar_bills = map(lambda bc: bc.bill, BillCommittee.objects.filter(committee=bill_committees[i].committee))[:3]
    bill_actions = BillAction.objects.filter(bill=bill)
    yay = bill.total_yes
    nay = bill.total_no

    user_yay = UserVote.objects.filter(bill=bill, vote='yay').count()
    user_nay = UserVote.objects.filter(bill=bill, vote='nay').count()

    print(user_yay)
    print(user_nay)

    already_voted = False
    user_vote = None

    try:
        profile = Profile.objects.get(user=request.user)
        user_vote_obj = UserVote.objects.get(user=profile, bill=bill)
        user_vote = 'Yay' if user_vote_obj.vote == 'yay' else 'Nay'
        already_voted = True
    except Exception:
        pass

    votes = {
        'users': {
            'total': user_yay + user_nay,
            'total_yes': user_yay,
            'total_no': user_nay
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
<<<<<<< HEAD
            'user_vote':user_vote,
            'already_voted':already_voted
=======
            'is_subscribed':is_subscribed,
>>>>>>> Added basic subscribe url
        }
    )
