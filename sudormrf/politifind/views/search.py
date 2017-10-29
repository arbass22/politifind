from django.shortcuts import render
from django.urls import reverse

def search(request):
    query = request.GET['q']
    results = [
        {
            "title": "I am a bill",
            "summary": "This is a summary of the result, it might be a short bill summary, or maybe a tagline for the politician.",
            "url": reverse('politician', args=(12,)),
        },
        {
            "title": "I am a bill",
            "summary": "This is a summary of the result, it might be a short bill summary, or maybe a tagline for the politician.",
            "url": reverse('politician', args=(12,)),
        },
        {
            "title": "I am a bill",
            "summary": "This is a summary of the result, it might be a short bill summary, or maybe a tagline for the politician.",
            "url": reverse('politician', args=(12,)),
        }
    ]
    return render(
        request,
        'search.html',
        context={'query':query,"results":results},
    )
