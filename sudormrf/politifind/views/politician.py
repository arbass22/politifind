from django.shortcuts import render

def politician(request, id):

    politician = {
        "name": "Bernie Sanders",
        "position": "Senator",
        "state": "Vermont",
        "image_url": "https://goo.gl/ZSzSK1",
        "party": "I",
        "facebook_handle": "@bernie",
        "twitter_hanlde": "@bernie",
        "youtube_handle": "@bernie",
    }

    committee_membership = [
        {
            "name": "Committee on the Budget",
            "tenure": 3
        },
        {
            "name": "Other Committee",
            "tenure": 5
        },
        {
            "name": "Socialist Committee",
            "tenure": 10
        }
    ]

    bill_sponsorship = [
        {
            "name": "Medicare for All Act of 2017",
            "code": "S.1804",
        },
        {
            "name": "Medicare for All Act of 2017",
            "code": "S.1804",
        },
        {
            "name": "Medicare for All Act of 2017",
            "code": "S.1804",
        },

    ]

    return render(
        request,
        'politician.html',
        context={
            'politician': politician,
            'committee_membership': committee_membership,
            'bill_sponsorship': bill_sponsorship
        },
    )
