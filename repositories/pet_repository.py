from db.run_sql import run_sql

from models.pet import Pet
from models.vet import Vet
import repositories.vet_repository as vet_repository


def save(pet):
    sql = "INSERT INTO pets (pet_name, date_of_birth, pet_type, owner_name, treatment_notes, vet_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING *"
    values = [pet.pet_name, pet.date_of_birth, pet.pet_type, pet.owner_name, pet.treatment_notes, pet.vet.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    pet.id = id
    return pet


def select_all():
    pets= []

    sql = "SELECT * FROM pets"
    results = run_sql(sql)

    for row in results:
        vet = vet_repository.select(row['vet_id'])
        pet = Pet(row['pet_name'], row['date_of_birth'], row['pet_type'], row['owner_name'], row['treatment_notes'], row['id'] )
        pet.assign_vet(vet)
        pets.append(pet)
    return pets



def select(id):
    pet = None
    sql = "SELECT * FROM pets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = vet_repository.select(result['vet_id'])
        pet = Pet(result['pet_name'], result['date_of_birth'], result['pet_type'], result['owner_name'], result['treatment_notes'], result['id'] )
        pet.assign_vet(vet)
    return pet


def delete_all():
    sql = "DELETE  FROM pets"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM pets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(pet):
    sql = "UPDATE pets SET (pet_name, date_of_birth, pet_type, owner_name, treatment_notes, vet_id) = (%s, %s, %s, %s, %s, %s) WHERE id = %s RETURNING *"
    values = [pet.pet_name, pet.date_of_birth, pet.pet_type, pet.owner_name, pet.treatment_notes, pet.vet.id, pet.id]
    run_sql(sql, values)