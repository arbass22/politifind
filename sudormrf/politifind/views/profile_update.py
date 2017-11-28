from django.shortcuts import redirect
from django.contrib.auth.models import User
from politifind.models import Profile, UserVote, Bill
from datetime import datetime

def profile_update(request):
    email = request.POST.get('email', None)
    party = request.POST.get('party', None)
    Profile.objects.filter(user=request.user).update(email=email, party=party)
    User.objects.filter(username=request.user).update(email=email)
    return redirect('profile')
