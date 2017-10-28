from django.db import models

###################################
## SIMPLE DATA (no foreign keys) ##
###################################

class User(models.Model):
    """
    Model representing all user info
    """
    uid = models.CharField(max_length=64, primary_key=True, help_text="Enter the id for the user")
    name = models.CharField(max_length=30, help_text="Enter the name of the user")
    username = models.CharField(max_length=20, help_text="Enter a username for the user")
    email = models.CharField(max_length=30, help_text="Enter the user's email")
    password = models.CharField(max_length=256, help_text="Enter a password for the user")
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
    sponsor_pid = models.ForeignKey('Politician', help_text="Enter the pid of the bill's sponsor", null=True)

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
    pid = models.ForeignKey('Politician', help_text="Enter the id of the voting politician")
    bid = models.ForeignKey('Bill', help_text="Enter the id of the bill being voted on")
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
    uid = models.ForeignKey('User', help_text="Enter the id of the voting user")
    bid = models.ForeignKey('Bill', help_text="Enter the id of the bill being voted on")
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
    chair_pid = models.ForeignKey('Politician', related_name='chair_pid', help_text="Enter the politician id of the chair", null=True)
    ranking_member_pid = models.ForeignKey('Politician', related_name='ranking_member_pid', help_text="Enter the politician id of the ranking member", null=True)

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
    name = models.CharField(max_length=200, help_text="Enter the name of this subcommittee", null=True)
    parent_cid = models.ForeignKey('Committee', related_name="parend_cid", help_text="Enter the id of the parent committee of this subcommittee")

class CommitteeMembership(models.Model):
    """
    Model representing the membership of a politician in a specific committee
    """
    cid = models.ForeignKey('Committee', help_text="Enter the id of the committee that this politician is a member of")
    pid = models.ForeignKey('Politician', help_text="Enter the id of the politician that is a member of the committee")
    relationship = models.CharField(max_length=30, help_text="Enter the politician's relationship to this committee")

class BillCommittee(models.Model):
    """
    Model representing the relationship between a bill and its associated committee
    """
    bid = models.ForeignKey('Bill', help_text="Enter the id of the bill")
    cid = models.ForeignKey('Committee', help_text="Enter the id of the committee")
    sid = models.ForeignKey('SubCommittee', null=True, help_text="Enter the id of the subcommittee")

#####################

############################
## MISC BILL ASSOCIATIONS ##
############################

class BillSponsorship(models.Model):
    """
    Model representing a sponsorship of a bill
    """
    bid = models.ForeignKey('Bill', help_text="Enter the id of the bill")
    pid = models.ForeignKey('Politician', help_text="Enter the id of the politician that is a sponsor of the bill")

class BillAction(models.Model):
    """
    Model representing an action on a bill
    """
    bid = models.ForeignKey('Bill', help_text="Enter the id of the bill")
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
    uid = models.ForeignKey('User', help_text="Enter the id of the voting user")
    pid = models.ForeignKey('Politician', help_text="Enter the id of the voting politician")
    date_subscribed = models.DateField(help_text="Enter the date that the user subscribed to this politician")

class UserBillSubscription(models.Model):
    """
    Model representing a user subscribing to a bill
    """
    uid = models.ForeignKey('User', help_text="Enter the id of the voting user")
    bid = models.ForeignKey('Bill', help_text="Enter the id of the bill being voted on")
    date_subscribed = models.DateField(help_text="Enter the date that the user subscribed to this bill")

class UserCommitteeSubscription(models.Model):
    """
    Model representing a user subscribing to a committee
    """
    uid = models.ForeignKey('User', help_text="Enter the id of the voting user")
    cid = models.ForeignKey('Committee', help_text="Enter the id of the committee")
    date_subscribed = models.DateField(help_text="Enter the date that the user subscribed to this committee")

#####################
