from datetime import date, timedelta
import calendar

from .models import Occasion

MOTHERS_DAY = 'Mother\'s Day'
FATHERS_DAY = 'Father\'s Day'
PARENT = 'Parent'
MALE = 'Male'
FEMALE = 'Female'
CURRENT_YEAR = date.today().year
SUNDAY = 6
MAY = 5
JUNE = 6
SECOND = 2
THIRD = 3
FIRST = 1


class AutomateOccasions():
    def __init__(self, recipient: object):
        self.recipient = recipient

    def get_nth_weekday(self, year: int, n: int, weekday: int, month: int) -> date:
        first_of_the_month = date(year, month, FIRST)
        first_weekday = first_of_the_month.weekday()
        if first_weekday != weekday:
            days_to_add = 6 - first_weekday
            first_weekday_date = (first_of_the_month +
                                  timedelta(days=days_to_add))
        else:
            first_weekday_date = first_of_the_month

        return first_weekday_date + timedelta(days=7 * (n - 1))

    def get_upcoming_date(self, holiday: str) -> date:
        '''Get the next date for the given holiday'''

        if holiday == MOTHERS_DAY:
            mothers_day_date = self.get_nth_weekday(
                CURRENT_YEAR, SECOND, SUNDAY, MAY)

            # if holiday is in the past get the next year's date
            if mothers_day_date < date.today():
                return self.get_nth_weekday(
                    CURRENT_YEAR + 1, SECOND, SUNDAY, MAY)
            else:
                return self.get_nth_weekday(
                    CURRENT_YEAR, SECOND, SUNDAY, MAY)

        if holiday == FATHERS_DAY:
            fathers_day_date = self.get_nth_weekday(
                CURRENT_YEAR, THIRD, SUNDAY, JUNE)

            # if holiday is in the past get the next year's date
            if fathers_day_date < date.today():
                return self.get_nth_weekday(
                    CURRENT_YEAR + 1, THIRD, SUNDAY, JUNE)
            else:
                return self.get_nth_weekday(
                    CURRENT_YEAR, THIRD, SUNDAY, JUNE)

    def auto_add_occasion(self, holiday: str):
        '''Add an occasion for the given holiday'''
        Occasion.objects.create(
            occasion_type=holiday,
            repeat_yearly=True,
            occasion_date=self.get_upcoming_date(holiday),
            description=f'{holiday} for {self.recipient.first_name} '
                        '{recipient.last_name}(auto-added)',
            recipient=self.recipient,
            user=self.recipient.user
        )

    @property
    def is_mother(self):
        return (self.recipient.relationship == PARENT
                and self.recipient.gender == FEMALE)

    @property
    def is_father(self):
        return (self.recipient.relationship == PARENT
                and self.recipient.gender == MALE)

    def process_occasions(self):
        '''Add occasions automatically for certain recipients
        based on information given in the recipient form'''

        if self.is_mother:
            self.auto_add_occasion(MOTHERS_DAY)

        elif self.is_father:
            self.auto_add_occasion(FATHERS_DAY)
