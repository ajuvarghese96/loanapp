from django.db import models

# Create your models here.


class LoanApplicant(models.Model):
    name = models.CharField(max_length=40, unique=True)
    nationality = models.CharField(max_length=20, null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=20, null=True)
    martial = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=20, null=True)
    id_type = models.CharField(max_length=20, null=True)
    id_no = models.IntegerField(null=True)
    address = models.CharField(max_length=20, null=True)
    email = models.EmailField(null=True)
    home_no = models.IntegerField(null=True)
    mobile = models.IntegerField(null=True)

    class Meta:
        verbose_name_plural = "LoanApplicant"

    def __str__(self):
        return self.name


LOAN_TYPE = ('Personal', 'Personal'), ('Vehicle', 'Vehicle'), ('Home', 'Home'), ('Education', 'Education')
LOAN_STATUS = ('Approved', 'Approved'), ('Processing', 'Processing'), ('Rejected', 'Rejected')


class LoanApplication(models.Model):
    application_num = models.IntegerField(unique=True)
    application_date = models.DateField()
    application_type = models.CharField(max_length=50, choices=LOAN_TYPE)
    finance_amount = models.IntegerField()
    finance_period = models.IntegerField()
    interest_rate = models.DecimalField(decimal_places=2,max_digits=5)
    loan_status = models.CharField(max_length=40, choices=LOAN_STATUS)
    existing_applicant = models.BooleanField()
    applicant_detail = models.ForeignKey(LoanApplicant, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "LoanApplication"

    def __str__(self):
        return self.applicant_detail.name

