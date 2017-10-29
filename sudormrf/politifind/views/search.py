from django.shortcuts import render

def search(request):
    query = request.GET['q']
    return render(
        request,
        'search.html',
        context={'query':query},
    )
