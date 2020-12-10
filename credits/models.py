from datetime import date
from django.db import models


class Program(models.Model):
    """Model for credit program"""
    name = models.CharField('Name of a program', max_length=50)
    min_sum = models.IntegerField('Minimal sum of a credit')
    max_sum = models.IntegerField('Maximum sum of a credit')
    min_age = models.IntegerField('Miniman age of a borrower')
    max_age = models.IntegerField('Maximum age of a borrower')

    def __str__(self):
        return str(self.name)


class Borrower(models.Model):
    """Model for person requests a credit"""
    iin = models.CharField('IIN of a borrower', max_length=12, unique=True)
    date_of_birth = models.DateField('Date of birth of a borrower')

    def __str__(self):
        return str(self.iin)

    @property
    def age(self):
        days_in_year = 365.2425
        age = int((date.today() - self.date_of_birth).days / days_in_year)
        return age


class Application(models.Model):
    """Model for credit application"""
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        related_name='requests',
        related_query_name='request',
        verbose_name='Application program'
    )
    borrower = models.ForeignKey(
        Borrower,
        on_delete=models.CASCADE,
        related_name='applications',
        related_query_name='application',
        verbose_name='Application borrower'
    )
    value = models.IntegerField('Sum of an application')
    status = models.BooleanField('Status of an application', blank=True, null=True)
    refusing_reason = models.TextField('Refusing reason of an application', blank=True, null=True)

    def __str__(self):
        return f'{self.borrower.iin} - {self.status}'


class Blacklist(models.Model):
    iin = models.OneToOneField(
        Borrower,
        on_delete=models.CASCADE,
        to_field='iin',
        related_name='+'
    )

    def __str__(self):
        return str(self.iin)
