from django.shortcuts import render
from politifind.models import Profile, PoliticianVote, Bill, UserBillSubscription, UserPoliticianSubscription, UserCommitteeSubscription

def index(request):
    recent_politician_news = PoliticianVote.objects.order_by('date_voted')[:3]
    recent_bill_news = Bill.objects.order_by('latest_action_date')[:3]
    if request.user.is_authenticated():
        user = Profile.objects.get(user=request.user)
        user_bill = UserBillSubscription.objects.filter(user=user).order_by('date_subscribed')[:3]
        user_politician = UserPoliticianSubscription.objects.filter(user=user).order_by('date_subscribed')[:3]
        user_committee = UserCommitteeSubscription.objects.filter(user=user).order_by('date_subscribed')[:3]
    else:
        user_bill = None
        user_politician = None
        user_committee = None
        
    
    return render(
        request,
        'index.html',
        context={
            'recent_politician_news': recent_politician_news,
            'recent_bill_news': recent_bill_news,
            'user_bill': user_bill,
            'user_politician': user_politician,
            'user_committee': user_committee,
        },
    )
