from django.db import models
from django.contrib.auth.models import User

###################################
## SIMPLE DATA (no foreign keys) ##
###################################

class Profile(models.Model):
    """
    Model representing all user info
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, help_text="Enter the name of the user")
    email = models.CharField(max_length=30, help_text="Enter the user's email")
    party = models.CharField(max_length=20, help_text="Select the user's political party")
    picture = models.CharField(max_length=200, help_text="Enter a url for the user's profile picture")

    def __str__(self):
        """
        String for representing a User
        """
        return '%s (%s)' % (self.name, self.party)

class Politician(models.Model):
    """
    Model representing a politician in Congress
    """
    pid = models.CharField(max_length=64, primary_key=True, help_text="Enter the id for the politician")
    name = models.CharField(max_length=30, help_text="Enter the name of the member")
    party = models.CharField(max_length=20, help_text="Select the member's political party")
    picture = models.CharField(max_length=200, help_text="Enter a url for the member's profile picture")
    state = models.CharField(max_length=2, help_text="Enter the member's state (two letter code)")
    title = models.CharField(max_length=20, help_text="Enter the member's title")
    twitter = models.CharField(max_length=200, null=True, help_text="Enter the url of the member's twitter profile")
    facebook = models.CharField(max_length=200, null=True, help_text="Enter the url of the member's facebook profile")
    youtube = models.CharField(max_length=200, null=True, help_text="Enter the url of the member's youtube profile")
    dob = models.DateField(help_text="Enter the date of birth of this member")
    missed_votes_pct = models.FloatField(null=True, help_text="Enter the percentage of missed votes")
    votes_with_party_pct = models.FloatField(null=True, help_text="Enter the percentage of votes with party")

    def __str__(self):
        """
        String for representing a Politician
        """
        return '%s (%s)' % (self.name, self.party)

class Bill(models.Model):
    """
    Model representing a bill
    """
    bid = models.CharField(max_length=64, primary_key=True, help_text="Enter the id for the bill")
    code = models.CharField(max_length=30, help_text="Enter the bill's code")
    name = models.CharField(max_length=200, help_text="Enter the name of the bill")
    status = models.CharField(max_length=20, null=True, help_text="Enter the status of the bill")
    subject = models.CharField(max_length=50, help_text="Enter the subject of the bill")
    summary = models.CharField(max_length=1000, help_text="Enter the summary of the bill")
    latest_action_date = models.DateField(help_text="Enter the date of the most recent action of the bill")
    latest_action = models.CharField(max_length=200, help_text="Enter the latest action of the bill")
    sponsor = models.ForeignKey('Politician', help_text="Enter the bill's sponsor", null=True)

    def __str__(self):
        """
        String representation of a Bill
        """
        return '%s: %s' % (self.code, self.name)

#####################

#################
## VOTE  DATA  ##
#################

class PoliticianVote(models.Model):
    """
    Model representing a given Politician's vote on a certain Bill
    """
    politician = models.ForeignKey('Politician', help_text="Enter the id of the voting politician")
    bill = models.ForeignKey('Bill', help_text="Enter the id of the bill being voted on")
    vote = models.CharField(max_length=15, help_text="Enter how the politician voted on this bill")
    date_voted = models.DateField(help_text="Enter the date of the politician's vote")

    def __str__(self):
        """
        String representation of a vote
        """
        return '%s: Politician %s voted %s on bill %s' % (self.pid, self.bid, self.vote, self.date_voted)

class UserVote(models.Model):
    """
    Model representing a given User's vote on a certain Bill
    """
    user = models.ForeignKey('Profile', help_text="Enter the id of the voting user")
    bill = models.ForeignKey('Bill', help_text="Enter the id of the bill being voted on")
    vote = models.CharField(max_length=15, help_text="Enter how the user voted on this bill")
    date_voted = models.DateField(help_text="Enter the date of the user's vote")

    def __str__(self):
        """
        String representation of a vote
        """
        return '%s: User %s voted %s on bill %s' % (self.uid, self.bid, self.vote, self.date_voted)

#####################

####################
## COMMITTEE DATA ##
####################

class Committee(models.Model):
    """
    Model representing a committee
    """
    cid = models.CharField(max_length=64, primary_key=True, help_text="Enter the id of the committee")
    name = models.CharField(max_length=200, help_text="Enter the name of this committee")
    chair = models.ForeignKey('Politician', related_name='chair', help_text="Enter the chair", null=True)
    ranking_member = models.ForeignKey('Politician', related_name='ranking_member', help_text="Enter the ranking member")
    chamber = models.CharField(max_length=20, null=True)

    def __str__(self):
        """
        String representation of a committee
        """
        return self.name

class SubCommittee(models.Model):
    """
    Model representing a subcomittee
    """
    sid = models.CharField(max_length=54, primary_key=True, help_text="Enter the id of this subcommittee (must also be a valid Committee)")
    name = models.CharField(max_length=200, help_text="Enter the name of this subcommittee")
    parent = models.ForeignKey('Committee', related_name="parent", help_text="Enter the parent committee of this subcommittee")

class CommitteeMembership(models.Model):
    """
    Model representing the membership of a politician in a specific committee
    """
    committee = models.ForeignKey('Committee', help_text="Enter the committee that this politician is a member of")
    politician = models.ForeignKey('Politician', help_text="Enter the politician that is a member of the committee")
    relationship = models.CharField(max_length=30, help_text="Enter the politician's relationship to this committee")

class BillCommittee(models.Model):
    """
    Model representing the relationship between a bill and its associated committee
    """
    bill = models.ForeignKey('Bill', help_text="Enter the bill")
    committee = models.ForeignKey('Committee', help_text="Enter the committee")
    subcommittee = models.ForeignKey('SubCommittee', help_text="Enter the subcommittee")

#####################

############################
## MISC BILL ASSOCIATIONS ##
############################

class BillSponsorship(models.Model):
    """
    Model representing a sponsorship of a bill
    """
    bill = models.ForeignKey('Bill', help_text="Enter the id of the bill")
    politician = models.ForeignKey('Politician', help_text="Enter the id of the politician that is a sponsor of the bill")

class BillAction(models.Model):
    """
    Model representing an action on a bill
    """
    bill = models.ForeignKey('Bill', help_text="Enter the id of the bill")
    action = models.CharField(max_length=50, help_text="Enter the action on the bill")
    action_date = models.DateField(help_text="Enter the date of the action")

#####################

#######################
## SUBSCRIPTION DATA ##
#######################

class UserPoliticianSubscription(models.Model):
    """
    Model representing a user subscribing to a politician
    """
    user = models.ForeignKey('Profile', help_text="Enter the subscribing user")
    politician = models.ForeignKey('Politician', help_text="Enter the subscribed politician")
    date_subscribed = models.DateField(help_text="Enter the date that the user subscribed to this politician")

class UserBillSubscription(models.Model):
    """
    Model representing a user subscribing to a bill
    """
    user = models.ForeignKey('Profile', help_text="Enter the id of the voting user")
    bill = models.ForeignKey('Bill', help_text="Enter the id of the bill being voted on")
    date_subscribed = models.DateField(help_text="Enter the date that the user subscribed to this bill")

class UserCommitteeSubscription(models.Model):
    """
    Model representing a user subscribing to a committee
    """
    user = models.ForeignKey('Profile', help_text="Enter the id of the voting user")
    committee = models.ForeignKey('Committee', help_text="Enter the id of the committee")
    date_subscribed = models.DateField(help_text="Enter the date that the user subscribed to this committee")

#####################
