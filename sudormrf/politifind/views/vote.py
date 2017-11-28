from django.shortcuts import redirect
from politifind.models import Profile, UserVote, Bill
from datetime import datetime

def vote(request, bid, user_vote):
    comment = request.POST.get('comment', None)
    bill = Bill.objects.get(bid=bid)
    profile = Profile.objects.get(user=request.user)
    new_user_vote = UserVote(user=profile, bill=bill, vote=user_vote, date_voted=datetime.now().date(), comment=comment)
    new_user_vote.save()
    return redirect('bill', bid)
