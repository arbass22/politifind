from django.shortcuts import render

def profile(request):

    user = {
      'username': 'justinkennedy10',
      'picture': 'https://www.tiecon.org/wp-content/uploads/2017/04/empty-profile-grey.jpg',
      'email': 'jekennedy@umass.edu',
      'party': 'Libertarian',
      'subscriptions': [
        {
          'type': 'bill',
          'link': 'bill/123',
          'title': 'S. 1866: Hurricanes Harvey, Irma, and Maria Education Relief Act of 2017',
          'description': 'A bill to provide the Secretary of Education with waiver authority for the reallocation rules and authority to extend the deadline by which funds have to be reallocated in the campus-based aid programs under the Higher Education Act of 1965 due to Hurricane Harvey, Hurricane Irma, and Hurricane Maria, to provide equitable services to children and teachers in private schools, and for other purposes.'
        }
      ]
    }

    return render(
        request,
        'profile.html',
        context={ 'user':user },
    )
