import unittest 

from models.vet import Vet

class TestVet(unittest.TestCase):

    def setUp(self):
        self.vet = Vet("Little Friends Vet Clinic 1")


    def test_vet_has_name(self):
        self.assertEqual("Little Friends Vet Clinic 1", self.vet.vet_name)

    

