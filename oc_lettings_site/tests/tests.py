from django.test import TestCase

class HomeViewTest(TestCase):

    def setUp(self):
        pass

    def test_home_url_exists_at_desired_location(self):
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_should_find_hyperlinks(self):
        response = self.client.get('/', follow_redirects=True)
        assert response.status_code == 200
        data = response.content.decode()
        text = "Lettings"
        assert text in data
        text = "Profiles"
        assert text in data
