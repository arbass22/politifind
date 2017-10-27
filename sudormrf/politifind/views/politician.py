from django.shortcuts import render


def politician(request, id, page=None):
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
            "status": "In committee",
        },
        {
            "name": "Othe bill that does something",
            "code": "S.1804",
            "status": "In committee"
        },
        {
            "name": "Here is a bill that has a long name since that is something that a lot of bills have",
            "code": "S.1804",
            "status": "Passed in House"
        },
    ]

    recent_votes = [
        {
            "name": "Medicare for All Act of 2017",
            "code": "S.1804",
            "vote": "Yay",
        },
        {
            "name": "Othe bill that does something",
            "code": "S.1804",
            "vote": "Nay",
        },
        {
            "name": "Here is a bill that has a long name since that is something that a lot of bills have",
            "code": "HR.123",
            "vote": "Yay",
        },
    ]

    context = {
        'politician': politician,
        'committee_membership': committee_membership,
        'bill_sponsorship': bill_sponsorship,
        'recent_votes': recent_votes,
    }

    if page == 'votes':
        return render(
            request,
            'politician_votes.html',
            context=context,
        )
    elif page == 'bills':
        return render(
            request,
            'politician_bills.html',
            context=context,
        )
    else:
        return render(
            request,
            'politician_home.html',
            context=context,
        )
