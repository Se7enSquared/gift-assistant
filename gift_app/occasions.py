from datetime import datetime, date
import calendar
import holidays

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


class AutomatedOccasions:

    def __init__(self, recipient):
        self.recipient = recipient

    def get_nth_weekday(self, year: int, n: int, weekday: int, month: int) -> date:
        daysInMonth = calendar.monthrange(year, month)[1]
        count = 0
        for day in range(1, daysInMonth):
            today = date(year, month, day)
            today_weekday = today.weekday()
            if today_weekday == weekday:
                count += 1
                if n == count:
                    return today

    def get_upcoming_date(self, holiday):
        '''Get the next date for the given holiday'''
        current_holidays = holidays.UnitedStates(years=CURRENT_YEAR)

        if holiday == MOTHERS_DAY:
            mothers_day_date = self.get_nth_weekday(CURRENT_YEAR, SECOND, SUNDAY, MAY)

            # if holiday is in the past get the next year's date
            if mothers_day_date < date.today():
                return self.get_nth_weekday(CURRENT_YEAR + 1, SECOND, SUNDAY, MAY)
            else:
                return self.get_nth_weekday(CURRENT_YEAR, SECOND, SUNDAY, MAY)

        if holiday == FATHERS_DAY:
            fathers_day_date = self.get_nth_weekday(CURRENT_YEAR, THIRD, SUNDAY, JUNE)

            # if holiday is in the past get the next year's date
            if fathers_day_date < date.today():
                return self.get_nth_weekday(CURRENT_YEAR + 1, THIRD, SUNDAY, JUNE)
            else:
                return self.get_nth_weekday(CURRENT_YEAR, THIRD, SUNDAY, JUNE)

    def auto_add_occasion(self, holiday):
        Occasion.objects.create(
            occasion_type=holiday,
            repeat_yearly=True,
            occasion_date=self.get_upcoming_date(holiday),
            description=f'{holiday} for {self.recipient.first_name} '
                        '{self.recipient.last_name}(auto-added)',
            recipient=self.recipient,
            user=self.recipient.user
        )

    def process_occasions(self):  # sourcery skip
        '''Add occasions automatically for certain recipients
        based on information given in the recipient form'''

        # TODO property
        if self.recipient.relationship == PARENT:
            if self.recipient.gender == FEMALE:
                self.auto_add_occasion(MOTHERS_DAY)
            if self.recipient.gender == MALE:
                self.auto_add_occasion(FATHERS_DAY)

        if self.recipient.birth_month > 0 and self.recipient.birth_day > 0:
            pass  # add recipient birthday
