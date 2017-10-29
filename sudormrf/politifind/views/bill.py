from django.shortcuts import render

def bill(request, id):
    
    bill = {
        'number': 'H.R.1314',
        'title': 'Bipartisan Budget Act of 2015',
        'subject': 'Economics and Public Finance',
        'sponsor': {
            'title': 'Rep.',
            'name': 'Pat Meehan',
            'state': 'PA',
            'party': 'R'
        },
        'passed': True,
        'summary': '(This measure has not been amended since the Senate agreed to the House amendment to the Senate amendment on October 30, 2015. The summary of that version is repeated here.) Bipartisan Budget Act of 2015 TITLE I--BUDGET ENFORCEMENT (Sec. 101) This bill amends the Balanced Budget and Emergency Deficit Control Act of 1985 to increase the discretionary spending limits for FY2016 and FY2017. The bill revises procedures for implementing the sequester of direct spending, which is required under current law and involves cuts that interact with discretionary spending levels. The bill requires the sequester to take place in FY2016 and FY2017 as if the amendments that this bill makes to the discretionary spending limits have not been made. It also adds an additional year to the sequester in FY2025 and adjusts the cuts required for Medicare. (Direct spending, also known as mandatory spending, is spending provided by laws other than appropriations bills. Sequestration is a process of automatic, usually across-the-board spending reductions under which budgetary resources are permanently cancelled to enforce specific budget policy goals.) The bill requires the discretionary spending limits in FY2016 and FY2017 to be increased by specified amounts for overseas contingency operations. (Sec. 102) The chairman of the Senate Budget Committee must file for publication in the Congressional Record committee allocations, aggregate spending and revenue levels, and levels of revenues and outlays for Social Security consistent with this bill. The chairman may also include reserve funds contained in the FY2016 budget resolution that are extended by one year. The bill provides that the allocations, aggregates, and levels submitted by the chairman are enforceable in the Senate as if they were included in a budget resolution conference agreement. The provisions in this section expire if Congress agrees to a budget resolution for FY2017. TITLE II--AGRICULTURE (Sec. 201) The bill amends the Federal Crop Insurance Act to require the Department of Agriculture (USDA) to renegotiate the Standard Reinsurance Agreement no later than December 31, 2016, and at least once every five years thereafter. (The Standard Reinsurance Agreement is an agreement between USDA and the private companies that administer the federal crop insurance program. It specifies details such as administrative and operating expense reimbursements and risk sharing between USDA and the companies in the operation of the program.) ...etc'
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

    bill_committees = [
        {
            'name': 'House Ways and Means Committee'
        }
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
            'similar_bills':similar_bills       
        }
    )
