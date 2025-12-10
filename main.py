from gestion_users import *
from authentification import connexion

def menu_principal(): 
    login, role, site = None, None, None

    print("Bienvenue dans la console de gestion du système d'information.")
    print("Veuillez vous authentifier.")
    
    while not login:
        login, role, site = connexion()

    print("\nConnexion réussie.")

    while True:
        print("\n**** Console de Gestion du Système d'Information **** ")
        print("1 - Gestion des Utilisateurs")
        print("2 - Gestion des Fichiers")
        print("3 - Gestion FTP / Réseau")
        print("0 - Quitter l'application")

        choix = input("Votre choix : ")
        print("--------------------------------")

        if choix == "1":
            if role in ["super-admin", "admin"]:
                menu_gestion_utilisateurs(login, site, role)
            else:
                print("Accès refusé : vous n'avez pas les droits pour ce menu.")

        elif choix == "2":
            print("\n Menu Gestion des Fichiers   pas encore implémenté.")
            input("Appuyez sur Entrée pour revenir au menu principal...")

        elif choix == "3":
            if role in ["super-admin", "admin"]:
                print("\n Menu Gestion FTP/Réseau   pas encore implémenté.")
            else:
                print("Accès refusé : vous n'avez pas les droits pour ce menu.")

        elif choix == "0":
            print("\n Fermeture de l'application. À bientôt.")
            break
        
        else:
            print("\n Choix invalide, merci de réessayer.")

def menu_gestion_utilisateurs(login, admin_site, admin_role): 
    while True:
        print("\n **** Menu Gestion des Utilisateurs ****")
        print("1 - Création d'un Utilisateur")
        print("2 - Modification d'un Utilisateur")
        print("3 - Suppression d'un Utilisateur")
        print("4 - Consultation des Utilisateurs")
        print("5 - Rechercher un utilisateur")
        print("0 - Retour au Menu Principal")

        choix = input("Votre choix : ")
        print("--------------------------------")

        if choix == "1":
            creer_utilisateur(admin_site, admin_role)
        elif choix == "2":
            modifier_utilisateur(admin_site, admin_role)
        elif choix == "3":
            supprimer_utilisateur(admin_site, admin_role)
        elif choix == "4":
            afficher_utilisateurs(admin_site, admin_role)
        elif choix == "5":
            rechercher_utilisateur()
        elif choix == "0":
            print("\n Retour au Menu Principal...")
            break
        else:
            print("\n Choix invalide, merci de réessayer.")

if __name__ == "__main__":
    menu_principal()
