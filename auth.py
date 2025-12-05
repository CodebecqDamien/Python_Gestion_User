import getpass
from datetime import datetime, timedelta
import json

FILE = "users.json"

def load_users():
    try:
        f = open(FILE, "r")
        users = json.load(f)
        f.close()
        for u in users:
            if u["locked_until"]:
                u["locked_until"] = datetime.fromisoformat(u["locked_until"])
        return users
    except:
        return []

def save_users(users):
    users_to_save = []
    for user in users:
        user_copy = user.copy()
        if user_copy["locked_until"]:
            user_copy["locked_until"] = user_copy["locked_until"].isoformat()
        users_to_save.append(user_copy)
    f = open(FILE, "w")
    f.write(json.dumps(users_to_save, indent=4))
    f.close()

def find_user(login, users):
    for user in users:
        if user["login"].strip().lower() == login.strip().lower():
            return user
    return None

def authentification():
    users = load_users()
    while True:
        print("----------------------------")
        login_input = input("Login : ")
        password_input = getpass.getpass("Mot de passe : ")

        user = find_user(login_input, users)
        if not user:
            print("Utilisateur inconnu")
            continue

        if user["locked_until"]:
            if datetime.now() < user["locked_until"]:
                print("Compte bloqué temporairement")
                print("Réessayez après :", user["locked_until"].strftime("%d/%m/%Y %H:%M:%S"))
                return None
            else:
                user["locked_until"] = None

        if user["password"] == password_input:
            print("Connexion réussie")
            user["tentatives_restantes"] = 3
            save_users(users)
            print("Bienvenue", user["prenom"], user["nom"], ",", user["role"], "du site", user["site"])
            return user

        user["tentatives_restantes"] -= 1
        print("Identifiants incorrects (", user["tentatives_restantes"], "tentatives restantes )")

        if user["tentatives_restantes"] <= 0:
            user["locked_until"] = datetime.now() + timedelta(minutes=15)
            user["tentatives_restantes"] = 3
            print("Compte bloqué pendant 15 minutes")

        save_users(users)
