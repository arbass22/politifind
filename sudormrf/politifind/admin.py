from django.contrib import admin

# Register your models here.

from .models import Profile, Politician, Bill, PoliticianVote, UserVote, Committee, SubCommittee, CommitteeMembership, BillCommittee, BillSponsorship, BillAction, UserPoliticianSubscription, UserBillSubscription, UserCommitteeSubscription

admin.site.register(Profile)
admin.site.register(Politician)
admin.site.register(Bill)
admin.site.register(PoliticianVote)
admin.site.register(UserVote)
admin.site.register(Committee)
admin.site.register(SubCommittee)
admin.site.register(CommitteeMembership)
admin.site.register(BillCommittee)
admin.site.register(BillSponsorship)
admin.site.register(BillAction)
admin.site.register(UserPoliticianSubscription)
admin.site.register(UserBillSubscription)
admin.site.register(UserCommitteeSubscription)


