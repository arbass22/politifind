import requests
from politifind.models import Bill, Politician

def run():
    api_header = { 'X-API-KEY': 'DB9r6gpgLzulQ9Z2GQKbWfLWXh9FtrK9utwjoFZk' }
    house = requests.get('https://api.propublica.org/congress/v1/115/house/bills/introduced.json', headers=api_header).json().get('results')[0].get('bills')
    senate = requests.get('https://api.propublica.org/congress/v1/115/senate/bills/introduced.json', headers=api_header).json().get('results')[0].get('bills')
    bills = house + senate
    for bill in bills:
        try:
            new_bill = Bill(bid=bill.get('bill_id'), code=bill.get('number'), name=bill.get('title'), status=bill.get('senate_passage') or bill.get('house_package'), subject=bill.get('primary_subject'), summary=bill.get('summary_short'), latest_action_date=bill.get('latest_major_action_date'), latest_action=bill.get("latest_major_action"), sponsor_pid=Politician.objects.get(pid=bill.get('sponsor_id')))
            new_bill.save()
        except Exception:
            pass

