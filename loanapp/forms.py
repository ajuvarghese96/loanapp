from django import forms



class applicants(forms.Form):
    TYPE = ('0', 'Select type'), ('Salaried', 'Salaried'), ('Self Employed', 'Self Employed'), ('Business', 'Business')
    GENDER = ('0', 'Select gender'), ('Male', 'Male'), ('Female', 'Female'), ('Trans', 'Trans')
    MARTIAL = ('0', 'Select status'), ('Single', 'Single'), ('Married', 'Married')

    
    Name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the full name'}))
    Nationality = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the Nationality '}))
    Applicant_Type = forms.ChoiceField(choices=TYPE, widget=forms.Select(attrs={'class': 'form-control'}))
    Gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(attrs={'class': 'form-control'}))
    Martial_status = forms.ChoiceField(choices=MARTIAL, widget=forms.Select(attrs={'class': 'form-control'}))
    Date_of_Birth = forms.DateField(required=True,
                                    widget=forms.SelectDateWidget(years=range(1900, 2022),
                                                                  attrs={'class': 'form-control'}))
    Identity_no = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the identity no.'}))
    Identity_type = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the identity'}))
    Address = forms.CharField(required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'height': '200px', 'placeholder': 'Enter the address'}))
    Email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter the email'}))
    Home_no = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the home contact number'}))
    Mobile = forms.IntegerField(required=True, widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter the Mobile number'}))


