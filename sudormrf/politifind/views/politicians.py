from django.shortcuts import render

def politicians(request):
    return render(
        request,
        'politicians.html',
        context={},
    )
