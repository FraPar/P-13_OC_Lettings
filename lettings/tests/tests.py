from django.test import TestCase
from django.urls import reverse

class LettingViewTest(TestCase):

    fixtures = [
                "address.json",
                "letting.json",
                ]

    def setUp(self):
        pass

    def test_lettings_url_exists_at_desired_location(self):
        response = self.client.get(reverse('lettings_index'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_should_find_title_in_lettings_index(self):
        response = self.client.get(reverse('lettings_index'), follow_redirects=True)
        assert response.status_code == 200
        data = response.content.decode()
        text = "Lettings"
        assert text in data

    def test_should_find_letting_in_lettings_index(self):
        response = self.client.get(reverse('lettings_index'), follow_redirects=True)
        assert response.status_code == 200
        data = response.content.decode()
        text = "Joshua Tree Green Haus /w Hot Tub"
        assert text in data

    def test_should_find_title_in_address(self):
        response = self.client.get(reverse('letting', args=[1]), follow_redirects=True)
        assert response.status_code == 200
        data = response.content.decode()
        text = "Joshua Tree Green Haus /w Hot Tub"
        assert text in data

    def test_should_find_address(self):
        response = self.client.get(reverse('letting', args=[1]), follow_redirects=True)
        assert response.status_code == 200
        data = response.content.decode()
        text = "7217 Bedford Street"
        assert text in data