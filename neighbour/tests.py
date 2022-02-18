from django.test import TestCase
from .models import NeighbourHood, Post, Profile,Business
# Create your tests here.

class NeighbourHoodTestClass(TestCase):
     # Set up method
    def setUp(self):
        self.highrise= NeighbourHood(name = 'Highrise', location ='Karen', occupants ='10')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.highrise,NeighbourHood))

    