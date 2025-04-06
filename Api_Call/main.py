import requests


base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_data(pokemon_name):
    url = f"{base_url}pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
pokemon_name = input("Enter the name of the Pokémon: ").lower()
pokemon_data = get_pokemon_data(pokemon_name)
print(pokemon_data)
if pokemon_data:
    print(f"Name: {pokemon_data['name']}")
    print(f"Height: {pokemon_data['height']}")
    print(f"Weight: {pokemon_data['weight']}")
    print("Abilities:")
    for ability in pokemon_data['abilities']:
        print(f"- {ability['ability']['name']}")