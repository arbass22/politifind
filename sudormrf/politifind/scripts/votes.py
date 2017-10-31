import random
import math
from politifind.models import Bill, Politician, PoliticianVote

def rand(maximum, minimum):
    return str(int(minimum + math.floor(random.random()*(maximum-minimum))))

def run():
    bills = Bill.objects.all()
    politicians = Politician.objects.all()
    for b in bills:
        for p in politicians:
            if random.random() < 0.5:
                vote = 'YAY'
            else:
                vote = 'NAY'
            y = rand(2017,2000)
            m = rand(12,1)
            d = rand(28,1)
            pv = PoliticianVote(pid=Politician.objects.get(pid=p.pid), bid=Bill.objects.get(bid=b.bid), vote=vote, date_voted=y+'-'+m+'-'+d)
            pv.save()


