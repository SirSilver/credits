from datetime import date, datetime


def parse_birth_date(iin):
    """Parse birth date from a given IIN"""
    year = iin[0:2]
    month = iin[2:4]
    day = iin[4:6]
    birth_date = datetime.strptime(f'{year}/{month}/{day}', '%y/%m/%d').date()

    return birth_date
