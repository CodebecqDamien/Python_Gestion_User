from gestion_users import *
from authentification import connexion_admin

def menu_principal():
    admin_login, admin_site = None, None

    print("Connexion admin obligatoire")
    while not admin_login:
        admin_login, admin_site = connexion_admin()

    while True:
        print("\n--- MENU PRINCIPAL ---")
        print("1 - Créer un utilisateur")
        print("2 - Modifier un utilisateur")
        print("3 - Supprimer un utilisateur")
        print("4 - Consulter les utilisateurs")
        print("5 - Rechercher un utilisateur")
        print("0 - Quitter")

        choix = input("Votre choix : ")

        if choix == "1":
            creer_utilisateur()
        elif choix == "2":
            modifier_utilisateur()
        elif choix == "3":
            supprimer_utilisateur(admin_login, admin_site)
        elif choix == "4":
            afficher_utilisateurs()
        elif choix == "5":
            rechercher_utilisateur()
        elif choix == "0":
            print("À bientôt !")
            break
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    menu_principal()
