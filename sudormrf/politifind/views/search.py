from django.shortcuts import render
from django.urls import reverse
from algoliasearch_django import raw_search
from politifind.models import Politician, Bill, Committee

def search(request):
    query = request.GET['q']
    params = { "hitsPerPage": 20 }

    politicianResponse = raw_search(Politician, query, params)
    committeeResponse = raw_search(Committee, query, params)
    billResponse = raw_search(Bill, query, params)

    results = []

    for politician in politicianResponse['hits']:
        results.append({
            'type': 'politician',
            'picture': politician['picture'],
            'name': politician['name'],
            'state': politician['state'],
            'party': politician['party'],
            'pid': politician['pid'],
            'title': politician['title']
        })

    for committee in committeeResponse['hits']:
        results.append({
            'type': 'committee',
            'cid': committee['cid'],
            'name': committee['name'],
            'chamber': committee['chamber']
        })

    for bill in billResponse['hits']:
        results.append({
            'type': 'bill',
            'bid': bill['bid'],
            'code': bill['code'],
            'name': bill['name'],
            'status': bill['status'],
            'subject': bill['subject']
        })

    print(len(results))

    return render(
        request,
        'search.html',
        context={'query':query,"results":results},
    )
