def menu_principal():    #fonction menu principal
    while True:
        print("\n**** Console de Gestion du Système d'Information **** ")
        print("1 - Gestion des Utilisateurs (T1)")
        print("2 - Gestion des Fichiers (T2)")
        print("3 - Gestion FTP / Réseau (T3)")
        print("0 - Quitter l'application")

        choix = input("Votre choix : ")

        if choix == "1":
            menu_gestion_utilisateurs() 

            print("\n Ouverture du menu T1 (Gestion des Utilisateurs)...")
            
        
        elif choix == "2":
            print("\n Menu Gestion des Fichiers (T2)  pas encore implémenté.")
            input("Appuyez sur Entrée pour revenir au menu principal...")

        
        elif choix == "3":
            print("\n Menu Gestion FTP/Réseau (T3)  pas encore implémenté.")
            input("Appuyez sur Entrée pour revenir au menu principal...")
        
        elif choix == "0":
            print("\n Fermeture de l'application. À bientôt.")
            break
        
        else:
            print("\n Choix invalide. Merci de réessayer.")


def menu_gestion_utilisateurs(): 
    while True:
        print("\n **** Menu Gestion des Utilisateurs (T1) ****")
        print("1 - Création d'un Utilisateur")
        print("2 - Modification d'un Utilisateur")
        print("3 - Suppression d'un Utilisateur")
        print("4 - Consultation des Utilisateurs")
        print("0 - Retour au Menu Principal")

        choix = input("Votre choix : ")

        if choix == "1":
            print("\n Création d'un utilisateur A FAIRE")
            # A FAIRE fonction creer_utilisateurs A FAIRE
            input("Appuyez sur Entrée pour continuer...")

        elif choix == "2":
            print("\n Modification d'un utilisateur A FAIRE")
            # A FAIRE  fonction  modifier_utilisateur 
            input("Appuyez sur Entrée pour continuer...")

        elif choix == "3":
            print("\n Suppression d'un utilisateur  A FAIRE ")
            # A FAIRE fonction  supprimer_utilisateur
            input("Appuyez sur Entrée pour continuer...")

        elif choix == "4":
            print("\n Consultation des utilisateurs A FAIRE")
            # A FAIRE fonction  consulter_utilisateurs
            input("Appuyez sur Entrée pour continuer...")

        elif choix == "0":
            print("\n Retour au Menu Principal...")
            break

        else:
            print("\n Choix invalide, merci de réessayer.")




    
if __name__ == "__main__":
    menu_principal()