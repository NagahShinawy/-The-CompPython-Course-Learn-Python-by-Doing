import datetime
from datetime import date, timedelta

DATETIME_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"


def now():
    return datetime.datetime.now().strftime(DATETIME_FORMAT)


def today():
    return date.today()


def yesterday():
    return (date.today() - timedelta(days=1)).strftime(DATE_FORMAT)


def tomorrow():
    return (date.today() + timedelta(days=1)).strftime(DATE_FORMAT)
