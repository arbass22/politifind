from random import randrange
from politifind.models import Politician, Committee, CommitteeMembership

def run():
    r = "member"
    politicians = Politician.objects.all()
    committees = Committee.objects.all()
    for p in politicians:
        i = randrange(0, 6)
        for i in range(0, i):
            random_index = randrange(0, len(committees))
            cm = CommitteeMembership(cid=Committee.objects.get(cid=committees[random_index].cid), pid=Politician.objects.get(pid=p.pid), relationship=r)
            cm.save()
