import json
import time
from django.core import serializers
from politifind.models import Bill, Politician, Committee

def run():
    bills_data = json.loads(serializers.serialize('json', Bill.objects.all()))
    bills = []
    for b in bills_data:
        fields = b.get('fields')
        bill = { 'bid': b.get('pk') }
        for k in fields:
            if k != 'summary':
                bill[k] = fields[k]
        bills.append(bill)

    politicians_data = json.loads(serializers.serialize('json', Politician.objects.all()))
    politicians = []
    for p in politicians_data:
        fields = p.get('fields')
        politician = { 'pid': p.get('pk') }
        for k in fields:
            politician[k] = fields[k]
        politicians.append(politician)

    committees_data = json.loads(serializers.serialize('json', Committee.objects.all()))
    committees = []
    for c in committees_data:
        fields = c.get('fields')
        committee = { 'cid': c.get('pk') }
        for k in fields:
            committee[k] = fields[k]
        committees.append(committee)

    with open('bills.json', 'w') as f:
        json.dump(bills, f)
