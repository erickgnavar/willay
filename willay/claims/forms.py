from django import forms

from .models import Claim


class ClaimForm(forms.ModelForm):

    class Meta:
        model = Claim
        fields = (
            'category', 'address', 'point',
            'description', 'photo',
        )

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        if self.request.user.is_authenticated:
            instance.user = self.request.user
            instance.save()
        return instance
