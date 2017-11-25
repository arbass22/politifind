import requests
import time
from politifind.models import Bill, Politician, PoliticianVote

def run():
    api_header = { 'X-API-KEY': '04bHoU8lq65ErglYL7Blrs4d9c0dlDe3D60kV3dc' }
    politicians = Politician.objects.all()
    bids = map(lambda b: b.bid, Bill.objects.all())
    count = 0
    for p in politicians:
        print "%d: %s" % (count, p.pid,)
        votes = requests.get('https://api.propublica.org/congress/v1/members/'+p.pid+'/votes.json', headers=api_header).json().get('results')[0].get('votes')
        for v in votes:
            bid = v.get('bill').get('bill_id')
            if bid not in bids:
                continue
            bill = Bill.objects.get(bid=bid)
            pv = PoliticianVote(politician=p, bill=bill, vote=v.get('position'), date_voted=v.get('date'))
            pv.save()
        count += 1
        if count % 10 == 0:
            time.sleep(4)
