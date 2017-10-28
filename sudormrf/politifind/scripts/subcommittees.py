import requests
from politifind.models import Committee, SubCommittee

def run():
    api_header = { 'X-API-KEY': 'DB9r6gpgLzulQ9Z2GQKbWfLWXh9FtrK9utwjoFZk' }
    house = requests.get('https://api.propublica.org/congress/v1/115/house/committees.json', headers=api_header).json().get('results')[0].get('committees')
    senate = requests.get('https://api.propublica.org/congress/v1/115/senate/committees.json', headers=api_header).json().get('results')[0].get('committees')
    committees = map(lambda c: { 'cid': c.get('id'), 'subcommittees': c.get('subcommittees') },house + senate)
    for c in committees:
        for s in c.get('subcommittees'):
            try:
                new_sc = SubCommittee(sid=s.get('id'), name=s.get('name'), parent_cid=Committee.objects.get(cid=c.get('cid')))
                new_sc.save()
            except Exception:
                pass

