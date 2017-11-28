from random import randrange
from itertools import chain
from django.shortcuts import render
from politifind.models import Profile, UserBillSubscription, UserCommitteeSubscription, UserPoliticianSubscription

def profile(request):
    user = Profile.objects.get(user=request.user)
    bill_subscriptions = UserBillSubscription.objects.filter(user=user)
    committee_subscriptions = UserCommitteeSubscription.objects.filter(user=user)
    politician_subscriptions = UserPoliticianSubscription.objects.filter(user=user)
    return render(
        request,
        'profile.html',
        context={ 'user':user, 'bill_subscriptions': bill_subscriptions, 'committee_subscriptions': committee_subscriptions, 'politician_subscriptions': politician_subscriptions },
    )
