import requests
import json  

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve data from the API.")
        return []  # Return an empty list if the request fails

    json_data = response.text  # Get the response text
    planets = json.loads(json_data)['bodies']  # Parse JSON data using json.loads()
    
    # Create a list to store planet information
    planet_info = []
    
    # Process each planet's information
    for planet in planets:
        if planet['isPlanet']:
            planet_info.append({
                'name': planet['englishName'],  # Get planet English name
                'mass': planet['mass']['massValue'],  # Get planet mass in kg
                'orbit_period': planet['sideralOrbit']  # Get planet orbit period in days
            })
            # Optionally print the planet info
            print(f"Planet: {planet['englishName']}, Mass: {planet['mass']['massValue']}, Orbit Period: {planet['sideralOrbit']} days")

    return planet_info  # Return the list of planets

def find_heaviest_planet(planets):
    # Check if planets list is empty
    if not planets:
        return None, None  # Return None values if the list is empty

    # Find the planet with the maximum mass
    heaviest_planet = max(planets, key=lambda p: p['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']  # Return the name and mass

# Fetch planet data
planets = fetch_planet_data()

# Find and print the heaviest planet
name, mass = find_heaviest_planet(planets)
if name and mass is not None:
    print(f"The heaviest planet is {name} with a mass of {mass} kg.")
else:
    print("Could not determine the heaviest planet.")
