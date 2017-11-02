from random import randrange
from itertools import chain
from django.shortcuts import render
from politifind.models import User, UserBillSubscription, UserCommitteeSubscription, UserPoliticianSubscription

def profile(request):
    users = User.objects.all()
    user = users[randrange(0,len(users))]
    bill_subscriptions = UserBillSubscription.objects.filter(uid__exact=user)
    committee_subscriptions = UserCommitteeSubscription.objects.filter(uid__exact=user)
    politician_subscriptions = UserPoliticianSubscription.objects.filter(uid__exact=user)
    return render(
        request,
        'profile.html',
        context={ 'user':user, 'bill_subscriptions': bill_subscriptions, 'committee_subscriptions': committee_subscriptions, 'politician_subscriptions': politician_subscriptions },
    )
