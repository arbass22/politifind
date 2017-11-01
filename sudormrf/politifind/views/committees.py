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
        "chair": {
                "name": "John Smith",
                "party_abr": "R",
                "summary": "Puppy from NY",
                "position": "Chair",
        },
        "ranking_member":{
            "name": "Puppy Pupperson",
            "summary": "Puppy from NY",
            "party_abr": "D",
            "position": "Ranking Member",
        },
    }
    page = {
        "tabs": [{
            "name": "Members",
            "url": "#",
            },
            {
            "name": "Bills",
            "url": "#",
            }],
        "active_tab": "Members"
    }

    return render(
        request,
        'committees.html',
        context={"committee":committee, "page":page},
    )
