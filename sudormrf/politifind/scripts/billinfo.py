import time
import requests
from politifind.models import Committee, Bill, BillCommittee, BillAction 

def run():
    api_header = { 'X-API-KEY': 'DB9r6gpgLzulQ9Z2GQKbWfLWXh9FtrK9utwjoFZk' }
    start, end = 745, 4000
    i = start
    bills = Bill.objects.all()[start:end]
    for b in bills:
        print '%d: updating %s' % (i,b.bid,)
        slug, congress = b.bid.split('-')
        bill_json = requests.get('https://api.propublica.org/congress/v1/'+congress+'/bills/'+slug+'.json', headers=api_header).json().get('results')[0]
        # update summary
        Bill.objects.filter(bid=b.bid).update(summary=bill_json.get('summary'))
        # get actions
        actions = bill_json.get('actions')
        for a in actions:
            ba = BillAction(bill=b, action=a.get('description'), action_date=a.get('datetime'))
            ba.save()
        # update votes
        votes = bill_json.get('votes')
        total_yes=0
        total_no=0
        for v in votes:
            if v.get('question') == 'On Passage':
                total_yes=v.get('total_yes')
                total_no=v.get('total_no')

        Bill.objects.filter(bid=b.bid).update(total_yes=total_yes, total_no=total_no)

        # get committees
        committees = bill_json.get('committee_codes')
        for c in committees:
            try:
                c_obj = Committee.objects.get(cid=c)
                bc = BillCommittee(bill=b, committee=c_obj)
                bc.save()
            except Exception:
                pass
        
        i+=1
        time.sleep(1)


