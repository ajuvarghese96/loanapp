from django.shortcuts import render,HttpResponseRedirect
from .forms import applicants
from .models import LoanApplicant
from .models import LoanApplication


# Create your views here.
def index(request):
    users = LoanApplication.objects.all()
    context = {'users':users}
    return render(request, 'index.html',context)




def apply(request):

    if request.method == "POST":
        form = applicants(request.POST)
        if form.is_valid():
            name = form.cleaned_data["Name"]
            nationality = form.cleaned_data["Nationality"]
            applicant_type = form.cleaned_data["Applicant_Type"]
            gender = form.cleaned_data["Gender"]
            martial_status = form.cleaned_data["Martial_status"]
            dob = form.cleaned_data["Date_of_Birth"]
            identity_no = form.cleaned_data["Identity_no"]
            identity_type = form.cleaned_data["Identity_type"]
            address = form.cleaned_data["Address"]
            email = form.cleaned_data["Email"]
            home_no = form.cleaned_data["Home_no"]
            mobile = form.cleaned_data["Mobile"]

            model_app = LoanApplicant(name=name, nationality=nationality, type=applicant_type, gender=gender,
                                              martial=martial_status,
                                              dob=dob, id_no=identity_no, id_type=identity_type, address=address, email=email,
                                              home_no=home_no, mobile=mobile)

            model_app.save()
        else:
            return HttpResponseRedirect('')
    else:
        form = applicants()
    context = {'form': form}
    return render(request,'application.html',context)


def view_detail(request, id):
    detail = LoanApplicant.objects.get(id=id)
    context = {'detail':detail}
    return render(request,'view.html',context)


