from django.test import TestCase

from ..models import User


class UserTestCase(TestCase):

    def test_str(self):
        user = User(username='test')
        self.assertEqual(str(user), 'test')
