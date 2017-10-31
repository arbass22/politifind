from django.shortcuts import render

def bills(request):
    return render(
        request,
        'bills.html',
        context={},
    )
