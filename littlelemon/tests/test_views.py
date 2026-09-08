from django.test import TestCase

class MenuViewTest(TestCase):
  def test_menu_view(self):
    response=self.client.get('/restaurant/menu/')
    self.assertEqual(response.status_code,200)