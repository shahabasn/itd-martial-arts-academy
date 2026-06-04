from django import forms

from .models import (
    Student,
    Batch,
    FeePackage,
    Staff,
    FeePayment,
    PoliceStation
)


class StaffLoginForm(forms.Form):

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Name'
            }
        )
    )

    pin = forms.CharField(
        max_length=10,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter PIN'
            }
        )
    )


class StudentForm(forms.ModelForm):
    
    class Meta:

        model = Student
        fields = '__all__'

        widgets = {
            'admission_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'fee_start_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
        }

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)

        self.fields['admission_date'].input_formats = ['%Y-%m-%d']
        self.fields['fee_start_date'].input_formats = ['%Y-%m-%d']
        self.fields['police_station'].queryset = PoliceStation.objects.filter(is_active=True)


class PoliceStationForm(forms.ModelForm):

    class Meta:
        model = PoliceStation
        fields = '__all__'

class BatchForm(forms.ModelForm):

    class Meta:

        model = Batch

        fields = '__all__'


class FeePackageForm(forms.ModelForm):

    class Meta:

        model = FeePackage

        fields = '__all__'


class FeePaymentForm(forms.ModelForm):

    class Meta:
        model = FeePayment
        fields = ['package', 'amount', 'paid_date', 'fee_start_date']
        widgets = {
            'paid_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
            'fee_start_date': forms.DateInput(
                attrs={'type': 'date'},
                format='%Y-%m-%d'
            ),
        }

    def __init__(self, *args, **kwargs):
        super(FeePaymentForm, self).__init__(*args, **kwargs)
        self.fields['paid_date'].input_formats = ['%Y-%m-%d']
        self.fields['fee_start_date'].input_formats = ['%Y-%m-%d']
        self.fields['package'].required = True
        self.fields['amount'].required = True
        self.fields['fee_start_date'].required = True

    def clean(self):
        cleaned_data = super().clean()
        package = cleaned_data.get('package')
        if package and not package.days:
            self.add_error('package', 'Selected package must specify validity days.')
        return cleaned_data
