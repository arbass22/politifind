from random import randrange
from politifind.models import Politician, Bill, BillSponsorship

def run():
    politicians = Politician.objects.all()
    bills = Bill.objects.all()
    for p in politicians:
        i = randrange(0, 6)
        for i in range(0, i):
            random_index = randrange(0, len(bills))
            bill = bills[random_index]
            bs = BillSponsorship(bid=Bill.objects.get(bid=bill.bid), pid=Politician.objects.get(pid=p.pid))
            bs.save()
