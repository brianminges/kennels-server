CUSTOMERS = [
    {
      "id": 1,
      "name": "Sydney Noh",
      "address": "976 Software School Rd.",
      "phone": "6152223333",
      "email": "snoh@gmail.com"
    },
    {
      "id": 2,
      "name": "Trevor Guinn",
      "address": "123 NSS Ln",
      "phone": "6152222222",
      "email": "tguinn@gmail.com"
    },
    {
      "id": 3,
      "name": "John \"No name\" Doe",
      "address": "456 Anywhere Road",
      "phone": "6153334444",
      "email": "jdoe@yahoo.com"
    },
    {
      "id": 4,
      "name": "Jane Johnson",
      "address": "789 Nowhere Road",
      "phone": "6154444444",
      "email": "jjohnson@gmail.com"
    }
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer