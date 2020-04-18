from django.test import TestCase

from .. import forms


class ExportClaimsFormTestCase(TestCase):
    def test_is_valid(self):
        attrs = {
            "category": "",
            "start_date": "2000-01-01",
            "end_date": "2000-01-02",
        }
        form = forms.ExportClaimsForm(attrs)
        self.assertTrue(form.is_valid())

    def test_is_not_valid(self):
        attrs = {
            "category": "",
            "start_date": "2000-01-02",
            "end_date": "2000-01-01",
        }
        form = forms.ExportClaimsForm(attrs)
        self.assertFalse(form.is_valid())
        self.assertIn("start_date", form.errors)
