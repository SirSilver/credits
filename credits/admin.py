from django.contrib import admin
from .models import Application, Blacklist, Borrower, Program


admin.site.register(Application)
admin.site.register(Blacklist)
admin.site.register(Borrower)
admin.site.register(Program)
