import json
import random
import string
import time

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

def generer_login(prenom, nom):
    return (prenom[0] + nom).lower()

def generer_pwd(taille=10):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(taille))

def creer_utilisateur():
    utilisateurs = charger_utilisateurs()

    prenom = input("Prénom : ")
    nom = input("Nom : ")
    login = generer_login(prenom, nom)
    pwd = generer_pwd()
    role = input("Rôle : ")
    site = input("Site : ")

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

def afficher_utilisateurs():
    utilisateurs = charger_utilisateurs()
    print("\n--- Liste des utilisateurs ---")
    for u in utilisateurs:
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

def modifier_utilisateur():
    utilisateurs = charger_utilisateurs()
    login = input("Login de l'utilisateur à modifier : ")
    for u in utilisateurs:
        if u["login"] == login:
            u["prenom"] = input(f"Nouveau prénom [{u['prenom']}] : ") or u['prenom']
            u["nom"] = input(f"Nouveau nom [{u['nom']}] : ") or u['nom']
            u["role"] = input(f"Nouveau rôle [{u['role']}] : ") or u['role']
            u["site"] = input(f"Nouveau site [{u['site']}] : ") or u['site']
            sauvegarder_utilisateurs(utilisateurs)
            print("Utilisateur modifié avec succès !")
            return
    print("Utilisateur introuvable.")

def supprimer_utilisateur(admin_login, admin_site):
    utilisateurs = charger_utilisateurs()
    login = input("Login de l'utilisateur à supprimer : ")

    for u in utilisateurs:
        if u["login"] == login:

            if admin_login == "admin" and admin_site == "Paris":
                utilisateurs.remove(u)
                sauvegarder_utilisateurs(utilisateurs)
                print("Utilisateur supprimé (super admin).")
                return

            if u["site"] == admin_site:
                utilisateurs.remove(u)
                sauvegarder_utilisateurs(utilisateurs)
                print("Utilisateur supprimé (admin local).")
                return

            print("Droits insuffisants pour supprimer cet utilisateur.")
            return

    print("Utilisateur introuvable.")
