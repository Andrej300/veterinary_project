from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.pet import Pet
import repositories.pet_repository as pet_repository
import repositories.vet_repository as vet_repository
import pdb

pets_blueprint = Blueprint("pets", __name__)

@pets_blueprint.route("/pets")
def pets():
    pets = pet_repository.select_all()
    return render_template("pets/index.html", all_pets = pets)

# NEW

@pets_blueprint.route("/pets/new", methods=['GET'])
def new_pet():
    vets = vet_repository.select_all()
    return render_template("pets/new.html", all_vets = vets)

# CREATE

@pets_blueprint.route("/pets", methods=['POST'])
def create_pet():
    pet_name    = request.form['Pet name']
    date_of_birth = request.form['Date of Birth']
    pet_type   = request.form['Pet type']
    owner_name = request.form['Owner name']
    treatment_notes = request.form['Treatment']
    vet  = vet_repository.select(request.form['vet_id'])

    pet = Pet(pet_name, date_of_birth, pet_type, owner_name, treatment_notes, vet)
    pet_repository.save(pet)
    return redirect('/pets')


# SHOW

@pets_blueprint.route("/pets/<id>", methods=['GET'])
def show_pet(id):
    pet = pet_repository.select(id)
    return render_template('pets/show.html', pet = pet)

# EDIT

@pets_blueprint.route("/pets/<id>/edit", methods=['GET'])
def edit_pet(id):
    pet = pet_repository.select(id)
    vets = vet_repository.select_all()
    return render_template('pets/edit.html', pet = pet, all_vets = vets)

# UPDATE

@pets_blueprint.route("/pets/<id>", methods=['POST'])
def update_pet(id):
    pet_name    = request.form['Pet name']
    date_of_birth = request.form['Date of birth']
    pet_type   = request.form['Pet type']
    owner_name = request.form['Owner name']
    treatment_notes = request.form['Treatment']
    vet  = vet_repository.select(request.form['vet_id'])
    pet = Pet(pet_name, date_of_birth, pet_type, owner_name, treatment_notes, vet, id)
    print(pet.vet.vet_name)
    pet_repository.update(pet)
    return redirect('/pets')

# DELETE

@pets_blueprint.route("/pets/<id>/delete", methods=['POST'])
def delete_pet(id):
    pet_repository.delete(id)
    return redirect('/pets')