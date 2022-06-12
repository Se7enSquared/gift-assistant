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

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    relationship = models.CharField(
        max_length=16, choices=RELATIONSHIP, default=SELECT)
    gender = models.CharField(max_length=10, choices=GENDER, default=SELECT)
    notes = models.TextField(blank=True, null=True)
    user_id = models.ForeignKey(
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

    def __str__(self):
        return f"{self.first_name} : {self.relationship}"

    class Meta:
        ordering = ["name"]


class Gift(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    gift_type = models.CharField(max_length=50)
    link = models.URLField(blank=True, null=True)
    given = models.BooleanField(default=False)
    occasion_id = models.ForeignKey(
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

    def __str__(self):
        return f"{self.title} : {self.link}"

    class Meta:
        ordering = ["title"]
