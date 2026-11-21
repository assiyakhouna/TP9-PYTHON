
import sqlite3


class SQLiteDAO:

    # Connexion à la base de données
    def __init__(self):
        self.conn = sqlite3.connect("boutique.db")
        self.cursor = self.conn.cursor()

        # Création des tables
        self.creer_tables()

        print("Connexion SQLite réussie !")

    # Créer les tables
    def creer_tables(self):

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS produits (
                id INTEGER PRIMARY KEY,
                nom TEXT NOT NULL,
                prix REAL NOT NULL
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY,
                nom TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)

        self.conn.commit()

    # Ajouter un produit
    def ajouter_produit(self, produit):
        try:
            sql = """
                INSERT INTO produits (id, nom, prix)
                VALUES (?, ?, ?)
            """

            valeurs = (produit.id, produit.nom, produit.prix)

            self.cursor.execute(sql, valeurs)
            self.conn.commit()

            print("Produit ajouté avec succès !")

        except sqlite3.IntegrityError:
            self.conn.rollback()
            print("Erreur : ID du produit déjà utilisé !")

        except sqlite3.Error as e:
            self.conn.rollback()
            print("Erreur SQLite :", e)

    # Ajouter un client
    def ajouter_client(self, client):
        try:
            sql = """
                INSERT INTO clients (id, nom, email)
                VALUES (?, ?, ?)
            """

            valeurs = (client.id, client.nom, client.email)

            self.cursor.execute(sql, valeurs)
            self.conn.commit()

            print("Client ajouté avec succès !")

        except sqlite3.IntegrityError:
            self.conn.rollback()
            print("Erreur : ID du client déjà utilisé !")

        except sqlite3.Error as e:
            self.conn.rollback()
            print("Erreur SQLite :", e)

    # Lister les produits
    def lister_produits(self):
        self.cursor.execute("SELECT * FROM produits")
        resultats = self.cursor.fetchall()

        if resultats:
            for ligne in resultats:
                print(ligne)
        else:
            print("Aucun produit trouvé !")

    # Lister les clients
    def lister_clients(self):
        self.cursor.execute("SELECT * FROM clients")
        resultats = self.cursor.fetchall()

        if resultats:
            for ligne in resultats:
                print(ligne)
        else:
            print("Aucun client trouvé !")

    # Rechercher un client par email
    def rechercher_client(self, email):
        sql = "SELECT * FROM clients WHERE email = ?"

        self.cursor.execute(sql, (email,))
        resultat = self.cursor.fetchone()

        if resultat:
            print("Client trouvé :", resultat)
        else:
            print("Client introuvable !")

    # Modifier le prix d'un produit
    def modifier_prix(self, id, nouveau_prix):
        sql = """
            UPDATE produits
            SET prix = ?
            WHERE id = ?
        """

        valeurs = (nouveau_prix, id)

        self.cursor.execute(sql, valeurs)
        self.conn.commit()

        if self.cursor.rowcount > 0:
            print("Prix modifié avec succès !")
        else:
            print("Produit introuvable !")

    # Fermer la connexion
    def fermer_connexion(self):
        self.cursor.close()
        self.conn.close()
        print("Connexion SQLite fermée !")
