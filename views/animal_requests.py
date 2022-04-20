# These are for challenge 1
# ANIMALS = [
#     {
#         "id": 1,
#         "name": "Snickers",
#         "species": "Dog",
#         "customerId": 4
#     },
#     {
#         "id": 2,
#         "name": "Brixton",
#         "species": "Dog",
#         "customerId": 1
#     },
#     {
#         "id": 3,
#         "name": "Blue",
#         "species": "Cat",
#         "customerId": 5
#     },
#     {
#         "id": 4,
#         "name": "Micky",
#         "species": "Mouse",
#         "customerId": 2
#     },
#     {
#         "id": 5,
#         "name": "Scooby",
#         "species": "Dog",
#         "customerId": 6
#     },
#     {
#         "id": 6,
#         "name": "Jack",
#         "species": "Rabbit",
#         "customerId": 3
#     }
# ]

# These are for challenge 2
ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "customerId": 4
    },
    {
        "id": 2,
        "name": "Brixton",
        "species": "Dog",
        "customerId": 1
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "customerId": 5
    },
    {
        "id": 4,
        "name": "Micky",
        "species": "Mouse",
        "customerId": 2
    },
    {
        "id": 5,
        "name": "Scooby",
        "species": "Dog",
        "customerId": 6
    },
    {
        "id": 6,
        "name": "Jack",
        "species": "Rabbit",
        "customerId": 3
    },
    {
        "id": 7,
        "name": "Winston",
        "species": "Dog",
        "customerId": 3
    },
    {
        "id": 8,
        "name": "Goofy",
        "species": "Dog",
        "customerId": 6
    },
    {
        "id": 8,
        "name": "Daisy",
        "species": "Cat",
        "customerId": 1
    },
    {
        "id": 10,
        "name": "Minnie",
        "species": "Mouse",
        "customerId": 2
    },
    {
        "id": 11,
        "name": "Scruffy",
        "species": "Dog",
        "customerId": 3
    },
    {
        "id": 12,
        "name": "Lucky",
        "species": "Rabbit",
        "customerId": 2
    }
]

def get_all_animals():
    return ANIMALS

# Function with a single parameter
def get_single_animal(id):
    # Variable to hold the found animal, if it exists
    requested_animal = None

    # Iterate the ANIMALS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for animal in ANIMALS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    # Get the id value of the last animal in the list
    max_id = ANIMALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    animal["id"] = new_id

    # Add the animal dictionary to the list
    ANIMALS.append(animal)

    # Return the dictionary with `id` property added
    return animal

def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)

def update_animal(id, new_animal):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value.
            ANIMALS[index] = new_animal
            break