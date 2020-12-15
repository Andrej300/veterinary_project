from db.run_sql import run_sql

from models.vet import Vet
from models.pet import Pet


def save(vet):
    sql = "INSERT INTO vets (vet_name) VALUES (%s) RETURNING *"
    values = [vet.vet_name]
    results = run_sql(sql, values)
    id = results[0]['id']
    vet.id = id
    return vet


def select_all():
    vets = []

    sql = "SELECT * FROM vets"
    results = run_sql(sql)

    for row in results:
        vet = Vet(row['vet_name'], row['id'] )
        vets.append(vet)
    return vets


def select(id):
    vet = None
    sql = "SELECT * FROM vets WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        vet = Vet(result['vet_name'], result['id'] )
    return vet


def delete_all():
    sql = "DELETE  FROM vets"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM vets WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(vet):
    sql = "UPDATE vets SET (vet_name) = (%s) WHERE id = %s"
    values = [vet.vet_name, vet.id]
    run_sql(sql, values)

def pets(vet):
    pets = []

    sql = "SELECT * FROM pets WHERE vet_id = %s"
    values = [vet.id]
    results = run_sql(sql, values)

    for row in results:
        pet = Pet(row['pet_name'], row['date_of_birth'], row['pet_type'], row['owner_name'],row['treatment_notes'], row['vet_id'], row['id'] )
        pets.append(pet)
    return pets