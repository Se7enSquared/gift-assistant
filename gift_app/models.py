from django.db import models
from gift_assist import settings

RELATIONSHIP = (
    "Spouse",
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

class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    profile_image = models.ImageField()


class Recipient(models.Model):
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    email = models.EmailField()
    relationship = models.CharField(
        max_length=16, choices=RELATIONSHIP, default="Spouse"
    )
    gender = models.CharField(max_length=10, choices=GENDER, default="Select Gender")
    notes = models.TextField(max_length=256)
    user_id = models.ForeignKey(
        "UserProfile",
        on_delete=models.SET_NULL,
    )
