from django import forms

from .models import (
    Student,
    Batch,
    FeePackage,
    Staff
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

class BatchForm(forms.ModelForm):

    class Meta:

        model = Batch

        fields = '__all__'


class FeePackageForm(forms.ModelForm):

    class Meta:

        model = FeePackage

        fields = '__all__'