// Create 'Pokemon' collection
db.createCollection("Pokemon");
db.Pokemon.createIndex({ pokemon_id: 1 }, { unique: true });

// Insert data into 'Pokemon' collection
db.Pokemon.insertMany([
  { pokemon_id: 1, name: 'Bulbasaur', primary_type: 'Grass', secondary_type: null },
  { pokemon_id: 2, name: 'Charmander', primary_type: 'Fire', secondary_type: null },
  { pokemon_id: 3, name: 'Squirtle', primary_type: 'Water', secondary_type: null },
  { pokemon_id: 4, name: 'Eevee', primary_type: 'Normal', secondary_type: null },
  { pokemon_id: 5, name: 'Pidgey', primary_type: 'Normal', secondary_type: 'Flying' }
]);

// Create 'Move' collection
db.createCollection("Move");
db.Move.createIndex({ move_id: 1 }, { unique: true });

// Insert data into 'Move' collection
db.Move.insertMany([
  { move_id: 1, name: 'Tackle', power: 35, type: 'Normal' },
  { move_id: 2, name: 'Water Gun', power: 40, type: 'Water' },
  { move_id: 3, name: 'Ember', power: 40, type: 'Fire' },
  { move_id: 4, name: 'Vine Whip', power: 40, type: 'Grass' },
  { move_id: 5, name: 'Wing Attack', power: 65, type: 'Flying' },
  { move_id: 6, name: 'Headbutt', power: 70, type: 'Normal' },
  { move_id: 7, name: 'Return', power: 100, type: 'Normal' }
]);

// Create 'Pokemon_Move' collection
db.createCollection("Pokemon_Move");

// Insert data into 'Pokemon_Move' collection
db.Pokemon_Move.insertMany([
  { pokemon_id: 1, move_id: 1 }, { pokemon_id: 1, move_id: 4 }, { pokemon_id: 1, move_id: 7 },
  { pokemon_id: 2, move_id: 1 }, { pokemon_id: 2, move_id: 3 }, { pokemon_id: 2, move_id: 7 },
  { pokemon_id: 3, move_id: 1 }, { pokemon_id: 3, move_id: 2 }, { pokemon_id: 3, move_id: 7 },
  { pokemon_id: 4, move_id: 1 }, { pokemon_id: 4, move_id: 6 }, { pokemon_id: 4, move_id: 7 },
  { pokemon_id: 5, move_id: 1 }, { pokemon_id: 5, move_id: 5 }, { pokemon_id: 5, move_id: 7 }
]);

// Create 'Type_Interactions' collection
db.createCollection("Type_Interactions");
db.Type_Interactions.createIndex({ attacking_type: 1, defending_type: 1 }, { unique: true });

// Insert data into 'Type_Interactions' collection
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

// Query to return all Pokémon who can learn 'Return'
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

// Query to return all moves in the game that are powerful against Grass
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
