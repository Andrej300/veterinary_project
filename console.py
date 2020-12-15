import pdb
from models.pet import Pet
from models.vet import Vet

import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository

# pet_repository.delete_all()
# vet_repository.delete_all()


vet_1 = Vet("Little Friends Vet Clinic 1")
vet_repository.save(vet_1)

vet_2 = Vet("Little Friends Vet Clinic 2")
vet_repository.save(vet_2)

pet1 = Pet("Leo", "15.08.2019.", "Cat", "John Smith", "Bacterial skin infection", vet_1)
pet_repository.save(pet1)
pet2 = Pet("Merlin", "02.04.2015.","Cat","William Campbell", "Allergic reaction", vet_1)
pet_repository.save(pet2)
pet3 = Pet("Charlie", "11.09.2012", "Dog","Danielle Johnson", "depression and loss of appetit", vet_2)
pet_repository.save(pet3)

