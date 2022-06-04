from django.contrib.auth.models import User
from django.db import models

from gift_assist import settings


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    profile_image = models.URLField()


class Recipient(models.Model):

    RELATIONSHIP = (
        (0, "Select Relationship"),
        (1, "Spouse"),
        (2, "Parent"),
        (3, "Sibling"),
        (4, "Friend"),
        (5, "Grandparent"),
        (6, "Cousin"),
        (7, "Coworker"),
        (1111, "Add Relationship"),
    )

    GENDER = (
        (0, "Select Gender"),
        (1, "Female"),
        (2, "Male"),
        (3, "Non-Binary"),
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField()
    relationship = models.CharField(max_length=16, choices=RELATIONSHIP, default=0)
    gender = models.CharField(max_length=10, choices=GENDER, default=0)
    notes = models.TextField()
    user_id = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.name} : {self.relationship}"

    class Meta:
        ordering = ["last_name"]
