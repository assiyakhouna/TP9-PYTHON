from mysql_dao import MySQLDAO
from produit import Produit
from client import Client

db = MySQLDAO()

# Ajouter un produit
p = Produit(1, "Ordinateur", 5000)
db.ajouter_produit(p)

# Ajouter un client
c = Client(1, "Assiya", "assiya@gmail.com")
db.ajouter_client(c)

# Lister les produits
print("\n--- Liste des produits ---")
db.lister_produits()

# Lister les clients
print("\n--- Liste des clients ---")
db.lister_clients()

# Rechercher un client
print("\n--- Recherche client ---")
db.rechercher_client("assiya@gmail.com")

# Modifier le prix
print("\n--- Modification du prix ---")
db.modifier_prix(1, 4500)

db.fermer_connexion()