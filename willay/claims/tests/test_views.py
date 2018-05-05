from django.contrib.auth.models import AnonymousUser
from django.contrib.messages.storage.fallback import FallbackStorage
from django.test import RequestFactory, TestCase
from django.urls import resolve, reverse
from mixer.backend.django import mixer

from .. import views


class ClaimCreateViewTestCase(TestCase):

    def setUp(self):
        self.view = views.ClaimCreateView.as_view()
        self.factory = RequestFactory()
        self.user = mixer.blend('users.User')
        self.category = mixer.blend('claims.Category')

    def test_match_expected_view(self):
        url = resolve('/claims/create/')
        self.assertEqual(url.func.__name__, self.view.__name__)

    def test_load_sucessful(self):
        request = self.factory.get('/')
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('form', response.context_data)

    def test_create_claim_anonymous_user(self):
        data = {
            'category': self.category.id,
            'address': 'test address',
            'description': 'description',
        }
        request = self.factory.post('/', data=data)
        request.user = AnonymousUser()
        request.session = {}
        request._messages = FallbackStorage(request)
        response = self.view(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], reverse('claims:claim-list'))

    def test_create_claim_with_logged_user(self):
        data = {
            'category': self.category.id,
            'address': 'test address',
            'description': 'description',
        }
        request = self.factory.post('/', data=data)
        request.user = self.user
        request.session = {}
        request._messages = FallbackStorage(request)
        response = self.view(request)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], reverse('claims:claim-list'))

    def test_create_claim_missing_fields(self):
        data = {
            'category': self.category.id,
        }
        request = self.factory.post('/', data=data)
        request.user = self.user
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context_data['form'].errors) > 0)


class ClaimListViewTestCase(TestCase):

    def setUp(self):
        self.view = views.ClaimListView.as_view()
        self.factory = RequestFactory()
        self.user = mixer.blend('users.User')

    def test_match_expected_view(self):
        url = resolve('/claims/')
        self.assertEqual(url.func.__name__, self.view.__name__)

    def test_load_sucessful(self):
        request = self.factory.get('/')
        request.user = self.user
        mixer.cycle(5).blend('claims.Claim')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('claims', response.context_data)
        self.assertIn('categories', response.context_data)
        self.assertEqual(response.context_data['claims'].count(), 5)


class ClaimDetailViewTestCase(TestCase):

    def setUp(self):
        self.view = views.ClaimDetailView.as_view()
        self.factory = RequestFactory()
        self.user = mixer.blend('users.User')
        self.claim = mixer.blend('claims.Claim')

    def test_match_expected_view(self):
        url = resolve('/claims/1/')
        self.assertEqual(url.func.__name__, self.view.__name__)

    def test_load_sucessful(self):
        request = self.factory.get('/')
        request.user = self.user
        response = self.view(request, id=self.claim.id)
        self.assertEqual(response.status_code, 200)
        self.assertIn('claim', response.context_data)
