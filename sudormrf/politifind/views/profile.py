from random import randrange
from django.shortcuts import render
from politifind.models import User

def profile(request):
    users = User.objects.all()
    user = users[randrange(0,len(users))]

    return render(
        request,
        'profile.html',
        context={ 'user':user },
    )
