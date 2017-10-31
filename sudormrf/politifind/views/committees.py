from django.shortcuts import render

def committees(request):
    committee = {
        "name": "Armed Forces Committee",
        "description": "The Senate Committee on Armed Services has legislative jurisdiction over military and defense",
        "makeup": {
            "total": 22,
            "republican": 10,
            "democrat": 10,
            "independent": 2,
        },
    }

    return render(
        request,
        'committees.html',
        context={"committee":committee},
    )
