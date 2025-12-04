def menu_principal():    #fonction menu principal
    while True:
        print("\n**** Console de Gestion du Système d'Information**** ")
        print("1 - Gestion des Utilisateurs (T1)")
        print("2 - Gestion des Fichiers (T2)")
        print("3 - Gestion FTP / Réseau (T3)")
        print("0 - Quitter l'application")

        choix = input("Votre choix : ")

        if choix == "1":
            menu_gestion_utilisateurs()

            print("\n Ouverture du menu T1 (Gestion des Utilisateurs)...")
            # appel fonction a faire 
            
        
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
    print("\n ****Menu Gestion des Utilisateurs (T1)****")

    input("Appuyez sur Entrée pour revenir au menu principal...")




    
if __name__ == "__main__":
    menu_principal()