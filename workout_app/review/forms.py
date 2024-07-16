from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):

    class Meta:
        model = Review
        fields = ["review_text", "rating"]
        widgets = {
            "review_text": forms.Textarea(attrs={"rows": 4, "cols": 40}),
            "rating": forms.NumberInput(
                attrs={"type": "number", "min": "1", "max": "5"}
            ),
        }
