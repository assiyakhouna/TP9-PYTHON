
from sqlite_dao import SQLiteDAO
from mysql_dao import MySQLDAO


def choisir_base_de_donnees():

    print("\n===== CHOIX DE LA BASE DE DONNEES =====")
    print("1. SQLite")
    print("2. MySQL")

    choix = input("Votre choix : ")

    if choix == "1":
        print("\nVous avez choisi SQLite.")
        return SQLiteDAO()

    elif choix == "2":
        print("\nVous avez choisi MySQL.")
        return MySQLDAO()

    else:
        print("\nChoix invalide !")
        return None


def afficher_menu():

    print("\n========== GESTION BOUTIQUE ==========")
    print("1. Ajouter un produit")
    print("2. Ajouter un client")
    print("3. Lister les produits")
    print("4. Lister les clients")
    print("5. Rechercher un client par email")
    print("6. Modifier le prix d'un produit")
    print("7. Quitter")

    choix = input("Votre choix : ")

    return choix

from produit import Produit
from client import Client


def lire_entier(message):
    while True:
        try:
            valeur = int(input(message))

            if valeur <= 0:
                print("Erreur : veuillez saisir un nombre positif !")
                continue

            return valeur

        except ValueError:
            print("Erreur : veuillez saisir un entier valide !")


def lire_prix(message):
    while True:
        try:
            prix = float(input(message))

            if prix <= 0:
                print("Erreur : le prix doit être positif !")
                continue

            return prix

        except ValueError:
            print("Erreur : veuillez saisir un prix valide !")

def executer_choix(db, choix):

    if choix == "1":
        id = lire_entier("ID du produit : ")
        nom = input("Nom du produit : ")
        prix = lire_prix("Prix du produit : ")

        produit = Produit(id, nom, prix)
        db.ajouter_produit(produit)

    elif choix == "2":
        id = lire_entier("ID du client : ")
        nom = input("Nom du client : ")
        email = input("Email du client : ")

        if "@" not in email or "." not in email:
            print("Erreur : email invalide !")
            return True

        client = Client(id, nom, email)
        db.ajouter_client(client)

    elif choix == "3":
        print("\n--- Liste des produits ---")
        db.lister_produits()

    elif choix == "4":
        print("\n--- Liste des clients ---")
        db.lister_clients()

    elif choix == "5":
        email = input("Email du client à rechercher : ")
        db.rechercher_client(email)

    elif choix == "6":
        id = lire_entier("ID du produit : ")
        nouveau_prix = lire_prix("Nouveau prix : ")

        db.modifier_prix(id, nouveau_prix)

    elif choix == "7":
        return False

    else:
        print("Choix invalide !")

    return True

def main():

    db = choisir_base_de_donnees()

    if db is None:
        return

    try:
        continuer = True

        while continuer:
            choix = afficher_menu()
            continuer = executer_choix(db, choix)

    except Exception as e:
        print("Une erreur est survenue :", e)

    finally:
        db.fermer_connexion()
        print("\nConnexion fermée.")
        print("Merci d'avoir utilisé notre application !")


if __name__ == "__main__":
    main()
