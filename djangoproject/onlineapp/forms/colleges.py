from onlineapp.models import *
from django import forms


class AddCollege(forms.ModelForm):
    class Meta:
        model = College
        exclude = ['id']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter location'}),
            'Acronym': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Acronym'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter contact'})
        }


class AddMockData(forms.ModelForm):
    class Meta:
        model = MockTestMarks
        exclude = ['id', 'student', 'total']
        widgets = {
            'problem1': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'problem1-marks'}),
            'problem2': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'problem2-marks'}),
            'problem3': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'problem3-marks'}),
            'problem4': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'problem4-marks'}),
        }


class AddStudent(forms.ModelForm):
    class Meta:
        model = Student
        exclude = ['id', 'dob', 'college']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'db_folder': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter db_folder'}),
            'dropped_out': forms.CheckboxInput(attrs={'class': 'form-control', 'placeholder': 'Enter droppedout'})
        }
