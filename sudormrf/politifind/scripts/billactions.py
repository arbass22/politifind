import random
from random import randrange
import math
from politifind.models import BillAction, Bill

def rand(maximum, minimum):
    return str(int(minimum + math.floor(random.random()*(maximum-minimum))))

def run():
    bills = Bill.objects.all()
    possible_actions = ["Introduced", "Amended", "Passed", "Vetoed", "Tabled", "Tossed"]
    for b in bills:
        rand_num_actions = randrange(0, 12)
        i = 0
        while(i < rand_num_actions):
            if(i==0):
                ba = BillAction(bid=Bill.objects.get(bid=b.bid), action=possible_actions[0], action_date=(rand(2017,2000)+'-'+rand(12,1)+'-'+rand(28,1)))
                ba.save()
            else:
                random_index = randrange(1, len(possible_actions))
                ba = BillAction(bid=Bill.objects.get(bid=b.bid), action=possible_actions[random_index], action_date=rand(2017,2000)+'-'+rand(12,1)+'-'+rand(28,1))
                ba.save()
                if(random_index == 2 or random_index == 3 or random_index == 5):
                    break
            i = i + 1
