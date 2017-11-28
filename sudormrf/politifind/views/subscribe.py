from politifind.models import Profile, UserBillSubscription

def subscribe(request, sub_type, bill_id):
    # do subscription 
    user = Profile.objects.filter(user=request.user)[0]
    
    print "hello from subscribe"
    return True
    if sub_type is 'bill':
        assoc = UserBillSubscription.objects.get_or_create(
            user=user, 
            bill=bill_id,
            date_subscribed=datetime.date.today(),
        )
    
def unsubscribe(type, id):
    # do unsubscribe
    print "hello from sunubscribe"
    return True

    