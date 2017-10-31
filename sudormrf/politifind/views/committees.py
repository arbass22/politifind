from django.shortcuts import render

def committees(request):
    return render(
        request,
        'committees.html',
        context={},
    )
