from django.core.exceptions import ObjectDoesNotExist
import requests
from .models import Blacklist


def check_sum(application, program):
    """Validate sum of an application"""
    value = application.value
    min_sum = program.min_sum
    max_sum = program.max_sum

    if value < min_sum:
        return False, 'Sum of application is less than a minimum for this credit program'
    elif value > max_sum:
        return False, 'Sum of application is more than a maximum for this credit program'
    return True, None


def check_age(application, program):
    """Validate age of a borrower"""
    age = application.borrower.age
    min_age = program.min_age
    max_age = program.max_age

    if age < min_age:
        return False, 'Borrower is younger than minimum age for this credit program'
    elif age > max_age:
        return False, 'Borrower is older than maximum age for this credit program'
    return True, None


def check_juridical(application):
    iin = application.borrower.iin
    url = 'https://stat.gov.kz/api/juridical/gov/'
    response = requests.get(url, params=f'bin={iin}&lang=ru')
    juridical = response.json()['success']
    if juridical:
        return False, 'Borrowers BIN is IE'
    return True, None

def check_blacklist(application):
    iin = application.borrower.iin
    try:
        exists = Blacklist.objects.get(iin=iin)
        return False, 'Borrower in a blacklist'
    except ObjectDoesNotExist:
        return True, None


def run_checks(application, program):
    status = True
    error = None
    while status != False:
        status, error = check_sum(application, program)
        if status == False: break
        status, error = check_age(application, program)
        if status == False: break
        status, error = check_juridical(application)
        if status == False: break
        status, error = check_blacklist(application)
        break
    return status, error
