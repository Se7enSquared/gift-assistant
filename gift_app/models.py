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
        "Select Relationship" "Spouse",
        "Parent" "Sibling",
        "Friend",
        "Grandparent",
        "Cousin",
        "Coworker",
        "Add Relationship",
    )

    GENDER = (
        "Select Gender",
        "Female",
        "Male",
        "Non-Binary",
    )

    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField()
    relationship = models.CharField(
        max_length=16, choices=RELATIONSHIP, default=RELATIONSHIP[0]
    )
    gender = models.CharField(max_length=10, choices=GENDER, default=GENDER[0])
    notes = models.TextField(max_length=256)
    user_id = models.ForeignKey(
        "User",
        on_delete=models.SET_NULL,
    )
