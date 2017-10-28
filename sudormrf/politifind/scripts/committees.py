import requests
from politifind.models import Committee, Politician

def run():
    api_header = { 'X-API-KEY': 'DB9r6gpgLzulQ9Z2GQKbWfLWXh9FtrK9utwjoFZk' }
    house = requests.get('https://api.propublica.org/congress/v1/115/house/committees.json', headers=api_header).json().get('results')[0].get('committees')
    senate = requests.get('https://api.propublica.org/congress/v1/115/senate/committees.json', headers=api_header).json().get('results')[0].get('committees')
    desired_keys = ['name', 'id', 'chair_id', 'subcommittees']
    committees = house + senate
    for c in committees:
        try:
            new_committee = Committee(cid=c.get('id'), name=c.get('name'), chair_pid=Politician.objects.get(pid=c.get('chair_id')), ranking_member_pid=Politician.objects.get(pid=c.get('ranking_member_id')))
            new_committee.save()
        except Exception:
            pass

