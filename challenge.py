from views import get_all_animals, get_all_customers
# from .animal_requests import ANIMALS
# from .customers_requests import CUSTOMERS

ANIMALS = get_all_animals()
CUSTOMERS = get_all_customers()

#CHALLENEGE 1
# def get_customer():
#     for animal in ANIMALS:
#         for customer in CUSTOMERS:
#             if customer["id"] == animal["customerId"]:
#                 print(f"{customer['name']} owns {animal['name']}")

# get_customer()

#CHALLENGE 2

def get_customer():
    for customer in CUSTOMERS:
        print(f"{customer['name']} is associated with the following animals:")
        for animal in ANIMALS:
             
            if customer["id"] == animal["customerId"]:          
                print(f"--{animal['name']}, {animal['species']}")

get_customer()