from django.test import TestCase

from .. import forms


class ExportClaimsFormTestCase(TestCase):

    def test_is_valid(self):
        form = forms.ExportClaimsForm({
            'category': '',
            'start_date': '2000-01-01',
            'end_date': '2000-01-02',
        })
        self.assertTrue(form.is_valid())

    def test_is_not_valid(self):
        form = forms.ExportClaimsForm({
            'category': '',
            'start_date': '2000-01-02',
            'end_date': '2000-01-01',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('start_date', form.errors)
