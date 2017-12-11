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
            'politician': politician,
        })

    for committee in committeeResponse['hits']:
        results.append({
            'type': 'committee',
            'committee': committee,
        })

    for bill in billResponse['hits']:
        results.append({
            'type': 'bill',
            'bill': bill,
        })

    print(len(results))

    return render(
        request,
        'search.html',
        context={'query':query,"results":results},
    )
