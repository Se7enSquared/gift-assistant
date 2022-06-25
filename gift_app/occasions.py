from dataclasses import dataclass
from datetime import date, timedelta

from .models import Occasion

MOTHERS_DAY = 'Mother\'s Day'
FATHERS_DAY = 'Father\'s Day'
PARENT = 'Parent'
MALE = 'Male'
FEMALE = 'Female'
CURRENT_YEAR = date.today().year
CURRENT_MONTH = date.today().month
SUNDAY = 6
MAY = 5
JUNE = 6
SECOND = 2
THIRD = 3
FIRST = 1
DAYS_IN_WEEK = 7


@dataclass
class IrregularHoliday:
    '''a dataclass for holidays that are not on a
        specific day of the month'''
    name: str
    month: int
    year: int
    weekday: int
    nth_day: int


def get_nth_weekday(holiday: IrregularHoliday) -> date:
    '''returns the date of the nth weekday of the month'''
    if CURRENT_MONTH > holiday.month:
        holiday.year += 1

    first_of_the_month = date(
        holiday.year, holiday.month, FIRST)
    first_weekday = first_of_the_month.weekday()
    if first_weekday != holiday.weekday:
        days_to_add = 6 - first_weekday
        first_weekday_date = (first_of_the_month +
                              timedelta(days=days_to_add))
    else:
        first_weekday_date = first_of_the_month

    days_left_to_find = holiday.nth_day - 1
    return first_weekday_date + timedelta(
        days=DAYS_IN_WEEK * (days_left_to_find))


class AutomateOccasions():
    def __init__(self, recipient: object):
        self.recipient = recipient

    def get_upcoming_date(self, holiday: str) -> date:
        '''Get the next date for the given holiday'''

        if holiday == MOTHERS_DAY:
            return self._find_irregular_holiday(MOTHERS_DAY, MAY, SECOND)
        if holiday == FATHERS_DAY:
            return self._find_irregular_holiday(FATHERS_DAY, JUNE, THIRD)

    def _find_irregular_holiday(self, name, month, nth_day):
        '''builds an irregular holiday object and finds the date of the
            next occurrence'''
        holiday = IrregularHoliday(
            name=name,
            month=month,
            year=CURRENT_YEAR,
            weekday=SUNDAY,
            nth_day=nth_day
        )

        holiday_date = get_nth_weekday(holiday)

        if holiday_date > date.today():
            return holiday_date

        # only in the case that the holiday is in the current month
        # this code may run
        holiday.year += 1
        return get_nth_weekday(holiday)

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
