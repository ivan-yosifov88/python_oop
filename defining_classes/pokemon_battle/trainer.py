from pokemon_battle.pokemon import Pokemon


class Trainer:

    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return "This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name: Pokemon):
        pokemon_for_release = [p for p in self.pokemon if p.name == pokemon_name]
        if not pokemon_for_release:
            return "Pokemon is not caught"
        self.pokemon.remove(pokemon_for_release[0])
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        trainer_name = self.name
        amount_of_pokemon_caught = len(self.pokemon)
        pokemon_details = '\n'.join(f'- {p.pokemon_details()}' for p in self.pokemon)
        return f"Pokemon Trainer {trainer_name}\nPokemon count {amount_of_pokemon_caught}\n{pokemon_details}"


pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
