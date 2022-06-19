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
        return f"{self.first_name} : {self.relationship}"

    class Meta:
        ordering = ["last_name"]


class Occasion(models.Model):
    name = models.CharField(max_length=50)
    occasion_type = models.CharField(max_length=50)
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
        return f"{self.name} : {self.occasion_date}"

    class Meta:
        ordering = ["name"]


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
    recipient = models.ForeignKey(
        Recipient,
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
        return f"{self.title} : {self.link}"

    class Meta:
        ordering = ["title"]
