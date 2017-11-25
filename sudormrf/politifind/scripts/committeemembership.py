import requests
import time
from random import randrange
from politifind.models import Politician, Committee, CommitteeMembership

def run():
    api_header = { 'X-API-KEY': 'DB9r6gpgLzulQ9Z2GQKbWfLWXh9FtrK9utwjoFZk' }
    committees = Committee.objects.all()
    for c in committees:
        members = requests.get('https://api.propublica.org/congress/v1/115/'+c.chamber.lower()+'/committees/'+c.cid+'.json', headers=api_header).json().get('results')[0].get('current_members')
        for member in members:
            p = Politician.objects.get(pid=member.get('id'))
            cm = CommitteeMembership(committee=c, politician=p, relationship='member')
            cm.save()
        time.sleep(2)
