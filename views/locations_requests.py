LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    },
    {
        "id": 2,
        "name": "Hendersonville",
        "address": "10854 Whatever Road"
    },
    {
        "id": 3,
        "name": "Nashville HQ",
        "address": "165 Broadway"
    }
]


def get_all_locations():
    return LOCATIONS

# Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the LOCATIONS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location