DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS pets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    vet_name VARCHAR(255),
    );

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    pet_name VARCHAR(255),
    date_of_birth VARCHAR(255),
    pet_type VARCHAR(255),
    treatment_notes TEXT,
    vet_id INT REFERENCES vets(id)
);

