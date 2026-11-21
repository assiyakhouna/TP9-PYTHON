
from sqlite_dao import SQLiteDAO
from produit import Produit
from client import Client

db = SQLiteDAO()

p1 = Produit(1, "Ordinateur", 5000)
c1 = Client(1, "Assia", "assia@gmail.com")

db.ajouter_produit(p1)
db.ajouter_client(c1)

print("\n--- Liste des produits ---")
db.lister_produits()

print("\n--- Liste des clients ---")
db.lister_clients()

print("\n--- Recherche client ---")
db.rechercher_client("assia@gmail.com")

print("\n--- Modification du prix ---")
db.modifier_prix(1, 4500)

print("\n--- Nouveau prix ---")
db.lister_produits()

db.conn.close()
