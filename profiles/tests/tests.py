from django.test import TestCase
from django.urls import reverse

class ProfileViewTest(TestCase):

    fixtures = [
                "profile.json",
                "user.json",
                ]

    def setUp(self):
        pass

    def test_profiles_url_exists_at_desired_location(self):
        response = self.client.get(reverse('profiles_index'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_should_find_profiles(self):
        response = self.client.get(reverse('profiles_index'), follow_redirects=True)
        assert response.status_code == 200
        data = response.content.decode()
        text = "HeadlinesGazer"
        assert text in data

    def test_should_find_profiles_details(self):
        response = self.client.get(reverse('profile', args=["HeadlinesGazer"]), follow_redirects=True)
        assert response.status_code == 200
        data = response.content.decode()
        text = "First name: Jamie"
        assert text in data