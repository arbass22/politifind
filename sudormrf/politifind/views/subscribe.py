import datetime
from django.http import HttpResponse
from politifind.models import Profile, UserBillSubscription, Bill

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
            date_subscribed=datetime.datetime.now()
        )

    return HttpResponse(status=200);
    
# do unsubscribe
def unsubscribe(request):
    item_type = request.POST.get("type")
    item_id = request.POST.get("id")
    user = Profile.objects.filter(user=request.user)[0]
    print item_type
    if item_type == 'bill':
        print "here"
        bill = Bill.objects.filter(bid=request.POST.get("id"))[0]
        (subscription, created) = UserBillSubscription.objects.filter(
            user=user, 
            bill=bill, 
            date_subscribed=datetime.datetime.now()
        ).delete()

    return HttpResponse(status=200);