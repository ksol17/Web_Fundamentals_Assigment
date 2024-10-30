import requests
import json

def fetch_pokemon_data(pokemon_name):
    """Fetch data for a specific Pokémon."""
    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data for {pokemon_name}.")
        return None
    
    json_data = response.text  # Get the response text
    return json.loads(json_data)  # Parse the JSON response and return it

def calculate_average_weight(pokemon_weights):
    """Calculate and return the average weight of the Pokémon."""
    total_weight = sum(pokemon_weights)
    average_weight = total_weight / len(pokemon_weights) if pokemon_weights else 0
    return average_weight

# List of Pokémon to fetch data for
pokemon_names = ["pikachu", "bulbasaur", "charmander"]
pokemon_data_list = []

# Fetch data for each Pokémon and store the information
for name in pokemon_names:
    data = fetch_pokemon_data(name)
    if data:  # Only append if data is successfully fetched
        pokemon_info = {
            'name': data['name'],
            'abilities': [ability['ability']['name'] for ability in data['abilities']],
            'weight': data['weight']  # Weight is in hectograms
        }
        pokemon_data_list.append(pokemon_info)

# Calculate and print individual average weight for each Pokémon
for pokemon in pokemon_data_list:
    average_weight = calculate_average_weight([pokemon['weight']])
    print(f"Pokémon: {pokemon['name'].capitalize()}")
    print(f"Abilities: {', '.join(pokemon['abilities']).capitalize()}")
    print(f"Weight: {pokemon['weight']} (hectograms)")
    print(f"Average Weight: {average_weight} (hectograms)\n")

# Calculate the overall average weight of all Pokémon
overall_average_weight = calculate_average_weight([p['weight'] for p in pokemon_data_list])
print(f"Overall Average Weight of Pokémon: {overall_average_weight} hectograms")
