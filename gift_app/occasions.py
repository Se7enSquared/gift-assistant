from datetime import date
import calendar

from .models import Occasion

MOTHERS_DAY = 'Mother\'s Day'
FATHERS_DAY = 'Father\'s Day'
BIRTHDAY = 'Birthday'
PARENT = 'Parent'
MALE = 'Male'
FEMALE = 'Female'
CURRENT_YEAR = date.today().year
NO_BIRTH_YEAR = 1900
SUNDAY = 6
MAY = 5
JUNE = 6
SECOND = 2
THIRD = 3


class InvalidHoliday(Exception):
    pass


class AutomateOccasions():
    def __init__(self, recipient, year=None) -> None:
        self.recipient = recipient
        self.year = year or CURRENT_YEAR
        self.birth_year = self.recipient.birth_year or NO_BIRTH_YEAR

    def process_birthday(self, month: int, day: int, year: int) -> date:
        if not month:
            raise ValueError('A month is required to process a birthday')
        if not day:
            raise ValueError('A day is required to process a birthday')

        birthday_date = date(year, month, day)
        self.auto_add_occasion(BIRTHDAY, birthday_date)

    def _get_nth_weekday(self, year: int, n: int, weekday: int, month: int) -> date:
        daysInMonth = calendar.monthrange(year, month)[1]
        count = 0
        for day in range(1, daysInMonth):
            today = date(year, month, day)
            today_weekday = today.weekday()
            if today_weekday == weekday:
                count += 1
                if n == count:
                    holiday = today
        if today < date.today():
            return self._get_nth_weekday(year + 1, n, weekday, month)
        return holiday

    def get_upcoming_holiday_date(self, holiday: str) -> date:
        '''Get the next date for the given holiday'''

        if holiday not in (MOTHERS_DAY, FATHERS_DAY):
            raise InvalidHoliday(f'{holiday} is not a valid holiday')

        if holiday == MOTHERS_DAY:
            n, weekday, month = SECOND, SUNDAY, MAY

        elif holiday == FATHERS_DAY:
            n, weekday, month = THIRD, SUNDAY, JUNE

        return self._get_nth_weekday(CURRENT_YEAR, n, weekday, month)

    def auto_add_occasion(self, holiday: str, occ_date=None, repeat=True):
        if not occ_date:
            occ_date = self.get_upcoming_holiday_date(holiday)
        Occasion.objects.create(
            occasion_type=holiday,
            repeat_yearly=repeat,
            occasion_date=occ_date,
            description=f'{holiday} for {self.recipient.first_name} '
                        f'{self.recipient.last_name}(auto-added)',
            recipient=self.recipient,
            user=self.recipient.user
        )

    @property
    def is_mother(self) -> bool:
        return (self.recipient.relationship == PARENT
                and self.recipient.gender == FEMALE)

    @property
    def is_father(self) -> bool:
        return (self.recipient.relationship == PARENT
                and self.recipient.gender == MALE)

    @property
    def has_birthday(self) -> bool:
        return (self.recipient.birth_month and self.recipient.birth_day)

    def process_occasions(self):
        '''Add occasions automatically for certain recipients
        based on information given in the recipient form'''

        if self.is_mother:
            self.auto_add_occasion(MOTHERS_DAY)

        elif self.is_father:
            self.auto_add_occasion(FATHERS_DAY)

        if self.has_birthday:
            self.process_birthday(
                self.recipient.birth_month,
                self.recipient.birth_day,
                self.birth_year
            )
