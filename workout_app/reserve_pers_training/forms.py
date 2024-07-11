from django import forms

from .models import Reserve


class ReservationForm(forms.ModelForm):

    date = forms.DateField(
        widget=forms.DateInput(
            attrs={"class": "form-control", "placeholder": "Enter Date"}
        )
    )
    start_time = forms.TimeField(
        widget=forms.TimeField(
            attrs={"class": "form-control", "placeholder": "Your password"}
        )
    )
    end_time = forms.TimeField(
        widget=forms.TimeField(
            attrs={"class": "form-control", "placeholder": "Your password"}
        )
    )
