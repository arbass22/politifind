from django.shortcuts import render
from politifind.models import Bill, BillCommittee

def bill(request, bid):
    bill = Bill.objects.get(bid=bid)
    bill_committees = BillCommittee.objects.filter(bid__exact=bid)

    votes = {
        'senate': {
            'date': 'November 14, 2017',
            'total': 110,
            'total_yes': 51,
            'total_no': 49,
            'total_not_voting': 10
        },
        'house': {
            'date': 'November 14, 2017',
            'total': 110,
            'total_yes': 47,
            'total_no': 53,
            'total_not_voting': 10
        },
        'users': {
            'date': 'November 14, 2017',
            'total': 100,
            'total_yes': 70,
            'total_no': 30
        }
    }

    bill_actions = [
        {
            'date': 'March 4, 2015',
            'description': 'Bill Introduced',
        },
        {
            'date': 'October 27, 2015',
            'description': 'Bill passed House',
        },
        {
            'date': 'October 29, 2015',
            'description': 'Bill passed Senate',
        },
        {
            'date': 'November 1, 2015',
            'description': 'Bill Enacted by P.O.T.U.S.',
        },
        {
            'date': 'November 1, 2015',
            'description': 'Bill became a law!',
        },
    ]

    similar_bills = [
        {
            'id': '12345',
            'number': 'H.R.2739',
            'title': 'Efficient Use of Government Spectrum Act of 2013',
            'passed': False,
            'sponsor': {
                'title': 'Rep',
                'name': 'Doris Matsui',
                'state': 'CA',
                'party': 'D'
            }
        },
        {
            'id': '12345',
            'number': 'H.R.2739',
            'title': 'Efficient Use of Government Spectrum Act of 2013',
            'passed': False,
            'sponsor': {
                'title': 'Rep',
                'name': 'Doris Matsui',
                'state': 'CA',
                'party': 'D'
            }
        },
        {
            'id': '12345',
            'number': 'H.R.2739',
            'title': 'Efficient Use of Government Spectrum Act of 2013',
            'passed': False,
            'sponsor': {
                'title': 'Rep',
                'name': 'Doris Matsui',
                'state': 'CA',
                'party': 'D'
            }
        },
    ]

    return render(
        request,
        'bill.html',
        context={
            'bill':bill,
            'bill_actions':bill_actions,
            'bill_committees':bill_committees,
            'similar_bills':similar_bills,
            'votes':votes,
        }
    )
