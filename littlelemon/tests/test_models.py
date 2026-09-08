from django.test import TestCase
from restaurant.models import Menu
class MenuTest(TestCase):
  def test_str_method(self):
    menu=Menu.objects.create(title='Pizza',price=10.99,inventory=5)
    self.assertEqual(str(menu),'Pizza : 10.99')