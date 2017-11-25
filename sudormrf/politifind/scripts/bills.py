import requests
import time
from politifind.models import Bill, Politician, BillSponsorship

def run():
    api_header = { 'X-API-KEY': 'DB9r6gpgLzulQ9Z2GQKbWfLWXh9FtrK9utwjoFZk' }

    politicians = Politician.objects.all()
    for p in politicians:
        p_bills = requests.get('https://api.propublica.org/congress/v1/members/'+p.pid+'/bills/introduced.json', headers=api_header).json().get('results')[0].get('bills')
        for bill in p_bills:
            try:
                new_bill = Bill(bid=bill.get('bill_id'), code=bill.get('number'), name=bill.get('title'), status=bill.get('senate_passage') or bill.get('house_package'), subject=bill.get('primary_subject'), summary=bill.get('summary_short'), latest_action_date=bill.get('latest_major_action_date'), latest_action=bill.get("latest_major_action"), sponsor=p)
                new_bill.save()
                sponsorship = BillSponsorship(bill=new_bill, politician=p)
                sponsorship.save()
            except Exception:
                pass
        time.sleep(5)
