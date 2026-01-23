import json
import random
import string
import hashlib

FICHIER = "data.json"

def charger_utilisateurs():
    try:
        with open(FICHIER, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def sauvegarder_utilisateurs(utilisateurs):
    with open(FICHIER, "w") as f:
        json.dump(utilisateurs, f, indent=4)

def generer_pwd():
    while True:
        try:
            taille = int(input("Choisir le nombre de caractères du mot de passe (minimum 10): "))
            if taille >= 10:
                break
            print("La taille minimale est de 10 caractères.\n")
        except ValueError:
            print("Veuillez entrer un nombre valide.\n")

    chars = string.ascii_letters + string.digits + string.punctuation

    # Génération du mot de passe
    pwd = "".join(random.choice(chars) for _ in range(taille))

    # Hachage
    pwd_hash = hashlib.sha256(pwd.encode()).hexdigest()

    return pwd, pwd_hash

def input_obligatoire(message):
    while True:
        valeur = input(message).strip()
        if valeur:
            return valeur
        print("Ce champ ne peut pas être vide !!")


def creer_utilisateur(admin_site, admin_role):
    utilisateurs = charger_utilisateurs()

    prenom = input_obligatoire("Prénom : ")
    nom = input_obligatoire("Nom : ")
    login = (prenom[0] + nom).lower()
    pwd, pwd_hash = generer_pwd()  # récupération du mot de passe et du hash 
    role = input_obligatoire("Rôle : ")
    site = input_obligatoire("Site : ")

    if admin_role == "admin" and role == "admin" :
        print("un administrateur ne peux pas crée un autre administrateur")
        return
    
    if admin_role != "super-admin" and site != admin_site :
        print("Vous ne pouvez créer que des utilisateurs de votre site ou vous devez être super-admin.")
        return
    
    for u in utilisateurs:
        if u["login"] == login:
            print("Login déjà existant. Création annulée.")
            return
            
    nouvel_user = {
        "prenom": prenom,
        "nom": nom,
        "login": login,
        "password": pwd_hash,
        "role": role,
        "site": site,
        "tentatives_restantes": 3,
        "locked_until": None
    }

    utilisateurs.append(nouvel_user)
    sauvegarder_utilisateurs(utilisateurs)
    print(f"\nUtilisateur créé ! Login : {login} | Password : {pwd}\n")

def menu_modification_utilisateur():
    print("\n**** Modification de l'utilisateur ****")
    print("1 - Modifier le prénom")
    print("2 - Modifier le nom")
    print("3 - Modifier le rôle")
    print("4 - Modifier le site")
    print("5 - Régénérer le mot de passe")
    print("0 - Quitter et sauvegarder")
    return input("Votre choix : ")

def modifier_utilisateur(admin_site, admin_role):
    utilisateurs = charger_utilisateurs()
    login = input("Login de l'utilisateur à modifier : ")

    for u in utilisateurs:
        if u["login"] == login:

            if admin_role != "super-admin" and u["site"] != admin_site:
                print("Vous n'avez pas les droits pour modifier un utilisateur d'un autre site.")
                return

            if admin_role == "admin" and u["role"] == "admin":
                print("Un administrateur ne peut pas modifier un autre administrateur.")
                return

            while True:
                choix = menu_modification_utilisateur()

                if choix == "1":
                    u["prenom"] = input_obligatoire(f"Nouveau prénom [{u['prenom']}] : ")
                    u["login"] = (u["prenom"][0] + u["nom"]).lower()
                    print(f"Nouveau login : {u['login']}")

                elif choix == "2":
                    u["nom"] = input_obligatoire(f"Nouveau nom [{u['nom']}] : ")
                    u["login"] = (u["prenom"][0] + u["nom"]).lower()
                    print(f"Nouveau login : {u['login']}")

                elif choix == "3":
                    if admin_role != "super-admin":
                        print("Seul un super-admin peut modifier le rôle.")
                    else:
                        u["role"] = input_obligatoire(f"Nouveau rôle [{u['role']}] : ")

                elif choix == "4":
                    if admin_role != "super-admin":
                        print("Seul un super-admin peut modifier le site.")
                    else:
                        u["site"] = input_obligatoire(f"Nouveau site [{u['site']}] : ")

                elif choix == "5":
                    pwd, pwd_hash = generer_pwd()
                    u["password"] = pwd_hash
                    print(f"Nouveau mot de passe : {pwd}")

                elif choix == "0":
                    sauvegarder_utilisateurs(utilisateurs)
                    print("Utilisateur modifié.")
                    return

                else:
                    print("Choix invalide.")
    else:
        print("Utilisateur introuvable.")

def supprimer_utilisateur(admin_site, admin_role):
    utilisateurs = charger_utilisateurs()
    login = input("Login de l'utilisateur à supprimer : ")
    
    if login == "sadmin":
        print("Impossible de supprimer le super-admin.")
        return

    for u in utilisateurs:
        if u["login"] == login:

            if admin_role == "utilisateur":
                print("Un administrateur ne peux pas supprimé un autre administrateur")
                return
            
            if admin_role != "super-admin" and u["site"] != admin_site:
                print("Vous ne pouvez supprimer que les utilisateurs de votre site.")
                return

            confirmation = input(f"Êtes-vous sûr de vouloir supprimer {login} ? (o/n) ")
            if confirmation.lower() == 'o':
                utilisateurs.remove(u)
                sauvegarder_utilisateurs(utilisateurs)
                print("Utilisateur supprimé.")
                return
            else:
                print("Suppression annulée.")
                return

    print("Utilisateur introuvable.")

def afficher_utilisateurs(admin_site, admin_role):
    utilisateurs = charger_utilisateurs()
    print("\n--- Liste des utilisateurs ---")

    for u in utilisateurs:
        if admin_role != "super-admin" and u["site"] != admin_site:
            continue
        print(f"{u['login']} - {u['prenom']} {u['nom']} ({u['role']}, {u['site']})")

def rechercher_utilisateur():
    utilisateurs = charger_utilisateurs()
    mot = input("Recherche (login / prénom / nom) : ").lower()
    trouve = False
    for u in utilisateurs:
        if mot in u['login'].lower() or mot in u['prenom'].lower() or mot in u['nom'].lower():
            print(f"{u['login']} - {u['prenom']} {u['nom']} ({u['role']}, {u['site']})")
            trouve = True
    if not trouve:
        print("Aucun utilisateur trouvé.")