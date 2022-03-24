from django.contrib import admin
from .models import LoanApplicant, LoanApplication

# Register your models here.
admin.site.register(LoanApplicant)
admin.site.register(LoanApplication)