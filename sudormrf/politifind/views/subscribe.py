import datetime
from django.http import HttpResponse
from politifind.models import Profile, Bill, Politician, Committee
from politifind.models import UserPoliticianSubscription, UserBillSubscription, UserCommitteeSubscription

# do subscription 
def subscribe(request):
    item_type = request.POST.get("type")
    item_id = request.POST.get("id")
    user = Profile.objects.filter(user=request.user)[0]
    
    if item_type == 'bill':
        bill = Bill.objects.filter(bid=item_id)[0]
        (subscription, created) = UserBillSubscription.objects.get_or_create(
            user=user, 
            bill=bill, 
            date_subscribed=datetime.datetime.now(),
            )
    elif item_type == 'politician':
        politician = Politician.objects.filter(pid=item_id)[0]
        (subscription, created) = UserPoliticianSubscription.objects.get_or_create(
            user=user,
            politician=politician,
            date_subscribed=datetime.datetime.now(),
            )
    elif item_type == 'committee':
        committee = Committee.objects.filter(cid=item_id)[0]
        (subscription, created) = UserCommitteeSubscription.objects.get_or_create(
            user=user,
            committee=committee,
            date_subscribed=datetime.datetime.now(),
            )
    else:
        HttpResponse(status=404);

    return HttpResponse(status=200);
    
# do unsubscribe
def unsubscribe(request):
    item_type = request.POST.get("type")
    item_id = request.POST.get("id")
    user = Profile.objects.filter(user=request.user)[0]

    if item_type == 'bill':
        bill = Bill.objects.filter(bid=item_id)[0]
        UserBillSubscription.objects.filter(
            user=user, 
            bill=bill, 
            ).delete()
    elif item_type == 'politician':
        politician = Politician.objects.filter(pid=item_id)[0]
        UserPoliticianSubscription.objects.filter(
            user=user,
            politician=politician,
            ).delete()
    elif item_type == 'committee':
        committee = Committee.objects.filter(cid=item_id)[0]
        UserCommitteeSubscription.objects.filter(
            user=user,
            committee=committee,
            ).delete()
    else:
        return HttpResponse(status=404)

    return HttpResponse(status=200);