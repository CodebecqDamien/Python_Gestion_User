import json
import random
import string

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

def generer_pwd(taille=10):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(taille))

def creer_utilisateur(admin_login, admin_site, admin_role):
    utilisateurs = charger_utilisateurs()

    prenom = input("Prénom : ")
    nom = input("Nom : ")
    login = (prenom[0] + nom).lower()
    pwd = generer_pwd()
    role = input("Rôle : ")
    site = input("Site : ")

    if admin_role != "super-admin" and site != admin_site:
        print("Vous ne pouvez créer que des utilisateurs de votre site.")
        return

    nouvel_user = {
        "prenom": prenom,
        "nom": nom,
        "login": login,
        "password": pwd,
        "role": role,
        "site": site,
        "tentatives_restantes": 3,
        "locked_until": None
    }

    utilisateurs.append(nouvel_user)
    sauvegarder_utilisateurs(utilisateurs)
    print(f"\nUtilisateur créé ! Login : {login} | Password : {pwd}\n")

def modifier_utilisateur(admin_login, admin_site, admin_role):
    utilisateurs = charger_utilisateurs()
    login = input("Login de l'utilisateur à modifier : ")

    for u in utilisateurs:
        if u["login"] == login:
            if admin_role != "super-admin" and u["site"] != admin_site:
                print("Vous n'avez pas les droits pour modifier un utilisateur d'un autre site.")
                return

            u["prenom"] = input(f"Nouveau prénom [{u['prenom']}] : ") or u['prenom']
            u["nom"] = input(f"Nouveau nom [{u['nom']}] : ") or u['nom']
            u["role"] = input(f"Nouveau rôle [{u['role']}] : ") or u['role']
            u["site"] = input(f"Nouveau site [{u['site']}] : ") or u['site']

            if admin_role != "super-admin" and u["site"] != admin_site:
                print("Un admin local ne peut pas changer le site d’un utilisateur.")
                return

            sauvegarder_utilisateurs(utilisateurs)
            print("Utilisateur modifié.")
            return

    print("Utilisateur introuvable.")

def supprimer_utilisateur(admin_login, admin_site, admin_role):
    utilisateurs = charger_utilisateurs()
    login = input("Login de l'utilisateur à supprimer : ")

    for u in utilisateurs:
        if u["login"] == login:
            if admin_role != "super-admin" and u["site"] != admin_site:
                print("Vous ne pouvez supprimer que les utilisateurs de votre site.")
                return

            utilisateurs.remove(u)
            sauvegarder_utilisateurs(utilisateurs)
            print("Utilisateur supprimé.")
            return

    print("Utilisateur introuvable.")

def afficher_utilisateurs(admin_login, admin_site, admin_role):
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
