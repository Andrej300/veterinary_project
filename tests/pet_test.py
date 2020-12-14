import unittest
from models.pet import Pet
from models.vet import Vet

class TestPet(unittest.TestCase):
    
    def setUp(self):
        self.pet = Pet("Leo", "30.01.2020", "dog", "Jack", "slight pain on front right leg","Little Friends Vet Clinic")

    def test_pet_has_name(self):
        self.assertEqual("Leo", self.pet.pet_name)

    def test_pet_has_date_of_birth(self):
        self.assertEqual("30.01.2020", self.pet.date_of_birth)

    def test_pet_has_type(self):
        self.assertEqual("dog", self.pet.pet_type)

    def test_pet_has_owner(self):
        self.assertEqual("Jack", self.pet.owner_name)

    def test_pet_has_treatment(self):
        self.assertEqual("slight pain on front right leg", self.pet.treatment_notes)

    def test_pet_has_vet(self):
        self.assertEqual("Little Friends Vet Clinic", self.pet.vet)



    

    