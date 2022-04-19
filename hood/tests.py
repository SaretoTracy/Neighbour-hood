from django.test import TestCase
from .models import Neighbourhood,Profile

# Create your tests here.
class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Prof= Profile( id = '1', user ='James',bio='Happy', profile_picture = 'example.jpg',email='chacha@gmail.com',phone_number='0724580020',neighbourhood='Membley' )
        
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.Prof,Profile)) 
