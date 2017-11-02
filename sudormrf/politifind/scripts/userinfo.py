import random
import math
from random import randrange
from politifind.models import User, UserVote, Bill, UserPoliticianSubscription, Politician, UserBillSubscription, Committee

def rand(maximum, minimum):
    return str(int(minimum + math.floor(random.random()*(maximum-minimum))))

def getADate():
    y = rand(2017, 2015)
    m = rand(12, 1)
    d = rand(28, 1)
    return y+'-'+m+'-'+d

def run():
    user0 = User(uid=0, name="Charlemain Augustus", username="caugustus", email="caugustus@email.com", password="compsci326", party="R", picture="http://placehold.it/150x150")
    user1 = User(uid=1, name="Adam Wolfe", username="awolfe", email="awolfe@email.com", password="compsci326", party="D", picture="http://placehold.it/150x150")
    user2 = User(uid=2, name="Bill Jensin", username="bjensin", email="bjensin@email.com", password="compsci326", party="R", picture="http://placehold.it/150x150")
    user3 = User(uid=3, name="Sara Autumne", username="sautumne", email="sautumn@email.com", password="compsci326", party="I", picture="http://placehold.it/150x150")
    user4 = User(uid=4, name="Veronika Hils", username="vhils", email="vhils@email.com", password="compsci326", party="R", picture="http://placehold.it/150x150")
    
    #user0.save()
    #user1.save()
    #user2.save()
    #user3.save()
    #user4.save()
    
    users = User.objects.all()
    bills = Bill.objects.all()
    ps = Politician.objects.all()
    cs = Committee.objects.all()
    for u in users:
        z = randrange(1, 5)
        i = 0
        while(i < z):
            i = i + 1
            x = random.random()
            if x < 0.5:
                v = "YAY"
            else:
                v = "NAY"
            r_index1 = randrange(0, len(bills))
            uv = UserVote(uid=User.objects.get(uid=u.uid).uid, bid=Bill.objects.get(bid=bills[r_index1].bid).bid, vote=v, date_voted=getADate())
            #uv.save()
        y = randrange(1,5)
        i = 0
        while(i < y):
            i = i + 1
            r_index2 = randrange(0, len(ps))
            ups = UserPoliticianSubscription(uid=User.objects.get(uid=u.uid).uid, pid=Politician.objects.get(pid=ps[r_index2].pid).pid, date_subscribed=getADate())
            #ups.save()
        i = 0
        w = randrange(1,5)
        while(i < w):
            i = i + 1
            r_index3 = randrange(0, len(bills))
            ubs = UserBillSubscription(uid=User.objects.get(uid=u.uid).uid, bid=Bill.objects.get(bid=bills[r_index3].bid).bid, date_subscribed=getADate())
            #ubs.save()
        i = 0
        k = randrange(1, 5)
        while(i < k):
            i = i + 1
            r_index4 = randrange(0, len(cs))
            ucs = UserCommitteeSubscription(uid=User.objects.get(uid=u.uid).uid, cid=Committee.objects.get(cid=cs[r_index4].cid).cid, date_subscribed=getADate())
            #ucs.save()
