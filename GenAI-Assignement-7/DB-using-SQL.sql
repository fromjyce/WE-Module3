USE pokemon_game;

CREATE TABLE Pokemon (
    pokemon_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    primary_type VARCHAR(20),
    secondary_type VARCHAR(20)
);

CREATE TABLE Move (
    move_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    power INT,
    type VARCHAR(20)
);

CREATE TABLE Pokemon_Move (
    pokemon_id INT,
    move_id INT,
    FOREIGN KEY (pokemon_id) REFERENCES Pokemon(pokemon_id),
    FOREIGN KEY (move_id) REFERENCES Move(move_id),
    PRIMARY KEY (pokemon_id, move_id)
);

-- Inserting Pokemon data
INSERT INTO Pokemon (name, primary_type, secondary_type) VALUES
('Bulbasaur', 'Grass', NULL),
('Charmander', 'Fire', NULL),
('Squirtle', 'Water', NULL),
('Eevee', 'Normal', NULL),
('Pidgey', 'Normal', 'Flying');

INSERT INTO Move (name, power, type) VALUES
('Tackle', 35, 'Normal'),
('Water Gun', 40, 'Water'),
('Ember', 40, 'Fire'),
('Vine Whip', 40, 'Grass'),
('Wing Attack', 65, 'Flying'),
('Headbutt', 70, 'Normal'),
('Return', 100, 'Normal');

INSERT INTO Pokemon_Move (pokemon_id, move_id) VALUES
(1, 1), (1, 4), (1, 7),
(2, 1), (2, 3), (2, 7),
(3, 1), (3, 2), (3, 7),
(4, 1), (4, 6), (4, 7),
(5, 1), (5, 5), (5, 7);

CREATE TABLE Type_Interactions (
    attacking_type VARCHAR(20),
    defending_type VARCHAR(20),
    effectiveness VARCHAR(10),
    PRIMARY KEY (attacking_type, defending_type)
);

INSERT INTO Type_Interactions (attacking_type, defending_type, effectiveness) VALUES
('Fire', 'Grass', 'Strong'),
('Fire', 'Water', 'Weak'),
('Grass', 'Water', 'Strong'),
('Grass', 'Fire', 'Weak'),
('Grass', 'Flying', 'Weak'),
('Water', 'Fire', 'Strong'),
('Water', 'Grass', 'Weak'),
('Flying', 'Grass', 'Strong');

SELECT p.name
FROM Pokemon p
JOIN Pokemon_Move pm ON p.pokemon_id = pm.pokemon_id
JOIN Move m ON pm.move_id = m.move_id
WHERE m.name = 'Return';

SELECT name
FROM Move
WHERE type IN ('Fire', 'Flying');



