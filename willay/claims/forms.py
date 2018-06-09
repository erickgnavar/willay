from django import forms
from django.utils.translation import ugettext as _

from .models import Category, Claim


class ClaimForm(forms.ModelForm):

    class Meta:
        model = Claim
        fields = (
            'category', 'address', 'point',
            'description', 'photo',
        )
        widgets = {
            'point': forms.HiddenInput,
        }

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

    def save(self, *args, **kwargs):
        instance = super().save(*args, **kwargs)
        if self.request.user.is_authenticated:
            instance.user = self.request.user
            instance.save()
        return instance


class ExportClaimsForm(forms.Form):

    start_date = forms.DateField(label=_('Start date'))
    end_date = forms.DateField(label=_('End date'))
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].widget.attrs.update({
            'data-provide': 'datepicker',
            'date-date-format': 'yyyy-mm-dd',
            'data-date-end-date': '0d',
        })
        self.fields['end_date'].widget.attrs.update({
            'data-provide': 'datepicker',
            'date-date-format': 'yyyy-mm-dd',
            'data-date-end-date': '0d',
        })

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        if start_date and end_date and end_date < start_date:
            self.add_error('start_date', _('The start date must be lower that end date'))
