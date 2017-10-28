import requests
from politifind.models import Politician

def run():
    api_header = { 'X-API-KEY': 'DB9r6gpgLzulQ9Z2GQKbWfLWXh9FtrK9utwjoFZk' }
    house = requests.get('https://api.propublica.org/congress/v1/115/house/members.json', headers=api_header).json().get('results')[0].get('members')
    senate = requests.get('https://api.propublica.org/congress/v1/115/senate/members.json', headers=api_header).json().get('results')[0].get('members')
    politicians = house + senate
    for p in politicians:
        new_politician = Politician(pid=p.get('id'), name=p.get('first_name')+' '+p.get('last_name'), party=p.get('party'), picture="https://placehold.it/150x150", state=p.get('state'), title=p.get('title'), twitter=p.get('twitter_account'), facebook=p.get('facebook_account'), youtube=p.get('youtube_account'), dob=p.get('date_of_birth'))
        new_politician.save()
