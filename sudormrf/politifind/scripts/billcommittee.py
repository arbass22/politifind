from random import randrange
from politifind.models import Committee, Bill, BillCommittee

def run():
    committees = Committee.objects.all()
    bills = Bill.objects.all()
    for b in bills:
        random_index = randrange(0, len(committees))
        committee = committees[random_index]
        bc = BillCommittee(bid=Bill.objects.get(bid=b.bid), cid=Committee.objects.get(cid=committee.cid))
        bc.save()
