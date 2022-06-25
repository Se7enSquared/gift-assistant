from telnetlib import BINARY
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    profile_image = models.URLField()


class Recipient(models.Model):
    SELECT = 'Select'

    FEMALE = 'Female'
    MALE = 'Male'
    NON_BINARY = 'Non-binary'

    WIFE = 'Wife'
    MOTHER = 'Mother'
    GRANDMOTHER = 'Grandmother'
    GIRLFRIEND = 'Girlfriend'
    DAUGHTER = 'Daughter'
    SISTER = 'Sister'
    AUNT = 'Aunt'

    HUSBAND = 'Husband'
    FATHER = 'Father'
    GRANDFATHER = 'Grandfather'
    BOYFRIEND = 'Boyfriend'
    SON = 'Son'
    BROTHER = 'Brother'
    UNCLE = 'Uncle'

    FIANCE = 'Fiance'
    FRIEND = 'Friend'
    COUSIN = 'Cousin'
    COWORKER = 'Coworker'
    OTHER = 'Other'

    FEMALE_RELATIONSHIPS = (
        (SELECT, 'Select'),
        (WIFE, 'Wife'),
        (MOTHER, 'Mother'),
        (GRANDMOTHER, 'Grandmother'),
        (FIANCE, 'Fiance'),
        (GIRLFRIEND, 'Girlfriend'),
        (DAUGHTER, 'Daughter'),
        (SISTER, 'Sister'),
        (AUNT, 'Aunt'),
        (FRIEND, 'Friend'),
        (COUSIN, 'Cousin'),
        (COWORKER, 'Coworker'),
        (OTHER, 'Other')
    )

    MALE_RELATIONSHIPS = (
        (SELECT, 'Select'),
        (HUSBAND, 'Husband'),
        (FATHER, 'Father'),
        (GRANDFATHER, 'Grandfather'),
        (FIANCE, 'Fiance'),
        (BOYFRIEND, 'Boyfriend'),
        (SON, 'Son'),
        (BROTHER, 'Brother'),
        (UNCLE, 'Uncle'),
        (FRIEND, 'Friend'),
        (COUSIN, 'Cousin'),
        (COWORKER, 'Coworker'),
        (OTHER, 'Other')
    )
    NON_BINARY_RELATIONSHIPS = tuple(
        set(FEMALE_RELATIONSHIPS + MALE_RELATIONSHIPS))

    GENDERS = [
        (FEMALE, FEMALE),
        (MALE, MALE),
        (NON_BINARY, NON_BINARY)
    ]

    GENDER_RELATIONSHIPS = {
        FEMALE: FEMALE_RELATIONSHIPS,
        MALE: MALE_RELATIONSHIPS,
        NON_BINARY: NON_BINARY_RELATIONSHIPS
    }

    MONTHS = [
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
        (12, "December"),
    ]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_month = models.IntegerField(choices=MONTHS, default=0)
    birth_day = models.IntegerField(null=True, blank=True)
    birth_year_unknown = models.BooleanField(default=False)
    birth_year = models.IntegerField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDERS,
                              default=GENDERS[0][0])
    relationship = models.CharField(
        max_length=16, choices=FEMALE_RELATIONSHIPS,
        default=FEMALE_RELATIONSHIPS[0][0])
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
        ("Dating Anniversary", "Dating Anniversary"),
        ("Work Anniversary", "Work Anniversary"),
        ("Mother's Day", "Mother's Day"),
        ("Father's Day", "Father's Day"),
        ("Valentine's Day", "Valentine's Day"),
    )

    occasion_type = models.CharField(max_length=50, choices=OCCASION_TYPES,
                                     default=OCCASION_TYPES[0][0])
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
        return (f"{self.recipient}'s"
                f"{self.occasion_type} | {self.occasion_date}")

    class Meta:
        ordering = ["recipient__last_name"]


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
