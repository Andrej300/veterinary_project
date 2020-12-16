DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    vet_name VARCHAR(255)
    );

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR(255),
    date_of_birth VARCHAR(255),
    pet_type VARCHAR(255),
    owner_name VARCHAR(255),
    treatment_notes VARCHAR(255),
    vet_id INT REFERENCES vets(id) ON DELETE CASCADE
);


