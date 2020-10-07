LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville",
        "locationId": 1,
        "address": "209 Emory Drive"
    },
    {
        "id": 2,
        "name": "Chicago",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "NewYork",
        "locationId": 2,
        "address": "8422 Johnson Pike"
    }
]

def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found animal, if it exists
    requested_location = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location
