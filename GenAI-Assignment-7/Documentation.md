# Designing a database for Pokemon!

## Problem Statement

We’re going to simplify Pokemon to just a couple of mechanics that are used in the game, and thankfully, you don’t need to know how it works to do this exercise.

Pokemon can have one or two ‘types,’ which decide whether they’re more effective or less effective against other Pokemon types. Every pokemon has a primay type; some also have a secondary type.

The game involves using moves to attack other Pokemon, and each move has a certain power and type. Every move has a set of Pokemon who are capable of learning it; and every Pokemon has a set of moves it can learn.

At the very least, we’d need database tables to store Pokemon, Type, and Move. However, ‘Pokemon’ and ‘Move’ have a classic many-to-many relationship. How do you deal with this?

1. Create all the tables needed. (5)
2. With the following details, populate the tables: (5)
    1. Bulbasaur is a pokemon of Grass type.
    2. Charmander is a pokemon of Fire type.
    3. Squirtle is a pokemon of Water type.
    4. Eevee is a pokemon of Normal type.
    5. Pidgey is a pokemon of the Normal/Flying type.
    6. Bulbasaur can learn Tackle, Vine Whip, and Return.
    7. Charmander can learn Tackle, Ember, and Return.
    8. Squirtle can learn Tackle, Water Gun, and Return.
    9. Eevee can learn Tackle, Headbutt, and Return.
    10. Pidgey can learn Tackle, Wing Attack, and Return.
    11. Tackle has 35 power and is Normal type.
    12. Water Gun has 40 power and is Water type.
    13. Ember has 40 power and is Fire type.
    14. Vine Whip has 40 power and is Grass type.
    15. Wing attack has 65 power and is Flying type.
    16. Headbutt has 70 power and is Normal type.
    17. Return has 100 power and is Normal type.
    18. Fire is powerful against Grass but weak to Water.
    19. Grass is powerful against Water but weak to both Fire and Flying.
    20. Water is powerful against Fire but weak to Grass.
    21. Normal is not weak to anything but not powerful against anything either.
    22. Flying is powerful against Grass and has no weaknesses.
3. Write a query that returns all the pokemon who can learn ‘Return’. (5)
4. Write a query that returns all the moves in the game that are powerful against Grass. (5)

## Using SQL

### Creating Tables
```sql
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

CREATE TABLE Type_Interactions (
    attacking_type VARCHAR(20),
    defending_type VARCHAR(20),
    effectiveness VARCHAR(10),
    PRIMARY KEY (attacking_type, defending_type)
);

```
### Populating Database with relevant records

```sql
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

INSERT INTO Type_Interactions (attacking_type, defending_type, effectiveness) VALUES
('Fire', 'Grass', 'Strong'),
('Fire', 'Water', 'Weak'),
('Grass', 'Water', 'Strong'),
('Grass', 'Fire', 'Weak'),
('Grass', 'Flying', 'Weak'),
('Water', 'Fire', 'Strong'),
('Water', 'Grass', 'Weak'),
('Flying', 'Grass', 'Strong');
```
### Writing SQL Queries for the following statements

#### Write a query that returns all the pokemon who can learn ‘Return’.
```sql
SELECT p.name
FROM Pokemon p
JOIN Pokemon_Move pm ON p.pokemon_id = pm.pokemon_id
JOIN Move m ON pm.move_id = m.move_id
WHERE m.name = 'Return';
```
#### Output
![1](Output%20Images\1.png)

#### Write a query that returns all the moves in the game that are powerful against Grass.
```sql
SELECT name
FROM Move
WHERE type IN ('Fire', 'Flying');
```
#### Output
![2](Output%20Images\2.png)

## Using No-SQL

### Populating Databases' collections with relevant records

```mongodb
db.createCollection("Pokemon");
db.Pokemon.createIndex({ pokemon_id: 1 }, { unique: true });

db.Pokemon.insertMany([
  { pokemon_id: 1, name: 'Bulbasaur', primary_type: 'Grass', secondary_type: null },
  { pokemon_id: 2, name: 'Charmander', primary_type: 'Fire', secondary_type: null },
  { pokemon_id: 3, name: 'Squirtle', primary_type: 'Water', secondary_type: null },
  { pokemon_id: 4, name: 'Eevee', primary_type: 'Normal', secondary_type: null },
  { pokemon_id: 5, name: 'Pidgey', primary_type: 'Normal', secondary_type: 'Flying' }
]);

db.createCollection("Move");
db.Move.createIndex({ move_id: 1 }, { unique: true });

db.Move.insertMany([
  { move_id: 1, name: 'Tackle', power: 35, type: 'Normal' },
  { move_id: 2, name: 'Water Gun', power: 40, type: 'Water' },
  { move_id: 3, name: 'Ember', power: 40, type: 'Fire' },
  { move_id: 4, name: 'Vine Whip', power: 40, type: 'Grass' },
  { move_id: 5, name: 'Wing Attack', power: 65, type: 'Flying' },
  { move_id: 6, name: 'Headbutt', power: 70, type: 'Normal' },
  { move_id: 7, name: 'Return', power: 100, type: 'Normal' }
]);

db.createCollection("Pokemon_Move");

db.Pokemon_Move.insertMany([
  { pokemon_id: 1, move_id: 1 }, { pokemon_id: 1, move_id: 4 }, { pokemon_id: 1, move_id: 7 },
  { pokemon_id: 2, move_id: 1 }, { pokemon_id: 2, move_id: 3 }, { pokemon_id: 2, move_id: 7 },
  { pokemon_id: 3, move_id: 1 }, { pokemon_id: 3, move_id: 2 }, { pokemon_id: 3, move_id: 7 },
  { pokemon_id: 4, move_id: 1 }, { pokemon_id: 4, move_id: 6 }, { pokemon_id: 4, move_id: 7 },
  { pokemon_id: 5, move_id: 1 }, { pokemon_id: 5, move_id: 5 }, { pokemon_id: 5, move_id: 7 }
]);

db.createCollection("Type_Interactions");
db.Type_Interactions.createIndex({ attacking_type: 1, defending_type: 1 }, { unique: true });

db.Type_Interactions.insertMany([
  { attacking_type: 'Fire', defending_type: 'Grass', effectiveness: 'Strong' },
  { attacking_type: 'Fire', defending_type: 'Water', effectiveness: 'Weak' },
  { attacking_type: 'Grass', defending_type: 'Water', effectiveness: 'Strong' },
  { attacking_type: 'Grass', defending_type: 'Fire', effectiveness: 'Weak' },
  { attacking_type: 'Grass', defending_type: 'Flying', effectiveness: 'Weak' },
  { attacking_type: 'Water', defending_type: 'Fire', effectiveness: 'Strong' },
  { attacking_type: 'Water', defending_type: 'Grass', effectiveness: 'Weak' },
  { attacking_type: 'Flying', defending_type: 'Grass', effectiveness: 'Strong' }
]);

```
### Writing No-SQL Queries for the following statements

#### Write a query that returns all the pokemon who can learn ‘Return’.
```mongodb
db.Pokemon.aggregate([
  { $lookup: {
      from: 'Pokemon_Move',
      localField: 'pokemon_id',
      foreignField: 'pokemon_id',
      as: 'moves'
    }
  },
  { $unwind: '$moves' },
  { $lookup: {
      from: 'Move',
      localField: 'moves.move_id',
      foreignField: 'move_id',
      as: 'move_info'
    }
  },
  { $unwind: '$move_info' },
  { $match: { 'move_info.name': 'Return' } },
  { $project: { _id: 0, pokemon_name: '$name' } }
]);
```
#### Output
![3](Output%20Images\3.png)

#### Write a query that returns all the moves in the game that are powerful against Grass.
```mongodb
db.Type_Interactions.aggregate([
  { $match: { defending_type: 'Grass', effectiveness: 'Strong' } },
  { $lookup: {
      from: 'Move',
      localField: 'attacking_type',
      foreignField: 'type',
      as: 'moves'
    }
  },
  { $unwind: '$moves' },
  { $project: { _id: 0, move_name: '$moves.name' } }
]);
```
#### Output
![4](Output%20Images\4.png)

## Differences in Experience Using Gen AI for SQL and NoSQL

### SQL Experience:
Working with Gen AI for SQL was straightforward and efficient. The generated SQL code provided clear instructions for creating tables, inserting data, and writing queries. The SQL syntax was familiar and easy to understand, making it simple to implement the database schema and execute the required queries. Additionally, the provided SQL queries efficiently handled complex operations such as joins and filtering, allowing for effective data retrieval.

### NoSQL Experience:
Using Gen AI for NoSQL, specifically for MongoDB, offered a different experience compared to SQL. The generated MongoDB queries were structured using MongoDB's aggregation framework, which required a slightly different approach compared to traditional SQL queries. While the syntax was different, the queries efficiently performed data aggregation and lookup operations necessary for retrieving the desired information from the NoSQL database. However, it required a bit more effort to understand and work with MongoDB's aggregation pipeline compared to SQL queries.

### Overall Comparison:
Both SQL and NoSQL experiences using Gen AI were positive, offering efficient solutions for designing databases and executing queries. SQL provided a more traditional relational database approach, which is well-suited for structured data and complex queries involving joins and relationships. On the other hand, NoSQL, particularly MongoDB, offered flexibility in schema design and scalability, making it suitable for unstructured or semi-structured data and distributed environments. Overall, Gen AI facilitated the process of working with both SQL and NoSQL databases, providing clear instructions and code snippets for database design and querying.
