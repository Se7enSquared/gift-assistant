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


def get_nth_weekday(year: int, n: int, weekday: int, month: int) -> date:
    daysInMonth = calendar.monthrange(year, month)[1]
    count = 0
    for day in range(1, daysInMonth):
        today = date(year, month, day)
        today_weekday = today.weekday()
        if today_weekday == weekday:
            count += 1
            if n == count:
                return today


def get_upcoming_date(holiday):
    '''Get the next date for the given holiday'''
    current_holidays = holidays.UnitedStates(years=CURRENT_YEAR)

    if holiday == MOTHERS_DAY:
        return get_nth_weekday(CURRENT_YEAR, SECOND, SUNDAY, MAY)
    if holiday == FATHERS_DAY:
        return get_nth_weekday(CURRENT_YEAR, THIRD, SUNDAY, JUNE)


def auto_add_occasion(occasion, recipient, request):
    Occasion.objects.create(
        occasion_type=occasion,
        repeat_yearly=True,
        occasion_date=get_upcoming_date(occasion),
        description=f'{occasion} for {recipient.first_name} '
                    '{recipient.last_name}(auto-added)',
        recipient=recipient,
        user=request.user
    )


def process_occasions(request, recipient):  # sourcery skip
    '''Add occasions automatically for certain recipients
    based on information given in the recipient form'''

    if recipient.relationship == PARENT:
        if recipient.gender == FEMALE:
            auto_add_occasion(MOTHERS_DAY, recipient, request)
        if recipient.gender == MALE:
            auto_add_occasion(FATHERS_DAY, recipient, request)

    if recipient.birth_month > 0 and recipient.birth_day > 0:
        pass  # add recipient birthday
