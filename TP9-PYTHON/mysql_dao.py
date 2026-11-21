
import mysql.connector


class MySQLDAO:

    # Constructeur : connexion à MySQL
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            port=3307,
            user="root",
            password="assiya2006",
            database="boutique"
        )

        self.cursor = self.conn.cursor()
        print("Connexion MySQL réussie !")

    # Ajouter un produit
    def ajouter_produit(self, produit):
        sql = """
        INSERT INTO produits (id, nom, prix)
        VALUES (%s, %s, %s)
        """

        valeurs = (produit.id, produit.nom, produit.prix)

        self.cursor.execute(sql, valeurs)
        self.conn.commit()

        print("Produit ajouté avec succès !")

    # Ajouter un client
    def ajouter_client(self, client):
        sql = """
        INSERT INTO clients (id, nom, email)
        VALUES (%s, %s, %s)
        """

        valeurs = (client.id, client.nom, client.email)

        self.cursor.execute(sql, valeurs)
        self.conn.commit()

        print("Client ajouté avec succès !")

    # Lister les produits
    def lister_produits(self):
        sql = "SELECT * FROM produits"

        self.cursor.execute(sql)
        resultats = self.cursor.fetchall()

        for ligne in resultats:
            print(ligne)

    # Lister les clients
    def lister_clients(self):
        sql = "SELECT * FROM clients"

        self.cursor.execute(sql)
        resultats = self.cursor.fetchall()

        for ligne in resultats:
            print(ligne)

    # Rechercher un client par email
    def rechercher_client(self, email):
        sql = "SELECT * FROM clients WHERE email = %s"

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
        SET prix = %s
        WHERE id = %s
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
