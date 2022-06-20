from django.contrib.auth.models import User
from django.db import models


SELECT = "select"


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    profile_image = models.URLField()


class Recipient(models.Model):

    RELATIONSHIP = (
        ("Select", "Select"),
        ("Spouse", "Spouse"),
        ("Parent", "Parent"),
        ("Child", "Child"),
        ("Sibling", "Sibling"),
        ("Friend", "Friend"),
        ("Grandparent", "Grandparent"),
        ("Cousin", "Cousin"),
        ("Coworker", "Coworker"),
        ("Other", "Other")
    )

    GENDER = (
        ("Select", "Select"),
        ("Female", "Female"),
        ("Male", "Male"),
        ("Non-Binary", "Non-Binary"),
    )

    MONTHS = (
        (0, "Select"),
        (1, "January"),
        (2, "February"),
        (3, "March"),
        (4, "April"),
        (5, "May"),
        (6, "June"),
        (7, "July"),
        (8, "August"),
        (9, "September"),
        (10, "October"),
        (11, "November"),
        (12, "December")
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_month = models.IntegerField(choices=MONTHS, default=0)
    birth_day = models.IntegerField(null=True, blank=True)
    birth_year_unknown = models.BooleanField(default=False)
    birth_year = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    relationship = models.CharField(
        max_length=16, choices=RELATIONSHIP, default=1)
    gender = models.CharField(max_length=10, choices=GENDER, default=SELECT)
    notes = models.TextField(blank=True, null=True)
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        ordering = ["last_name"]


class Occasion(models.Model):

    OCCASION_TYPES = (
        ("Birthday", "Birthday"),
        ("Wedding Anniversary", "Wedding Anniversary"),
        ("Wedding Anniversary", "Dating Anniversary"),
        ("Work Anniversary", "Work Anniversary"),
        ("Friendship Anniversary", "Friendship Anniversary"),
        ("Mother's Day", "Mother's Day"),
        ("Father's Day", "Father's Day"),
        ("Graduation", "Graduation"),
        ("Baby Shower", "Baby Shower"),
        ("New Baby", "New Baby"),
        ("Wedding", "Wedding"),
        ("House Warming", "House Warming"),
        ("Thanks", "Thanks"),
        ("Christmas", "Christmas"),
        ("Easter", "Easter"),
        ("Chinese New Year", "Chinese New Year"),
        ("Valentine's Day", "Valentine's Day"),
        ("Just Because", "Just Because"),
        ("Other", "Other"),
    )

    occasion_type = models.CharField(max_length=50,
                                     choices=OCCASION_TYPES,
                                     default="BIRTHDAY")
    repeat_yearly = models.BooleanField(default=False)
    occasion_date = models.DateField()
    description = models.TextField(blank=True, null=True)
    recipient = models.ForeignKey(
        Recipient,
        null=True,
        on_delete=models.SET_NULL,
    )
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.recipient}'s {self.occasion_type} | {self.occasion_date} "

    class Meta:
        ordering = ["recipient"]


class Gift(models.Model):

    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    gift_type = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)
    given = models.BooleanField(default=False)
    date_given = models.DateField(null=True, blank=True)
    occasion = models.ForeignKey(
        Occasion,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    user = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.title} | {self.link}"

    class Meta:
        ordering = ["title"]
