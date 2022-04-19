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

class NeighbourhoodTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.Juja = Location.objects.create(name="Juja")
        self.test_neighbourhood = Neighbourhood.objects.create(name='Membley',location='Nairobi',admin='Chacha',image='example.jpg',description='Beautiful place',occupants='1')
        self.test_neighbourhood.save()


    def test_save_method(self):
        self.test_neighbourhood.save()
        test_neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(test_neighbourhoods) > 0)
            
    
    def test_delete_method(self):
        self.Neighbourhood.delete_neighbourhood()
        neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods)==0)   
        
    def tearDown(self):
        Neighbourhood.objects.all().delete()
        
        

  