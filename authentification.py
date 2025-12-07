from gestion_users import charger_utilisateurs, sauvegarder_utilisateurs
import time
import getpass

BLOCAGE = 15 * 60

def connexion():
    utilisateurs = charger_utilisateurs()
    login = input("Login : ")
    pwd = getpass.getpass("Mot de passe : ")

    for u in utilisateurs:
        if u["login"] == login:

            if u["locked_until"] and time.time() < u["locked_until"]:
                reste = int((u["locked_until"] - time.time()) // 60)
                print(f"Compte verrouillé. Réessayez dans {reste} min.")
                return None, None, None

            if u["password"] == pwd:
                u["tentatives_restantes"] = 3
                u["locked_until"] = None
                sauvegarder_utilisateurs(utilisateurs)
                return u["login"], u["role"], u["site"]

            else:
                u["tentatives_restantes"] -= 1
                print(f"Mot de passe incorrect. Tentatives restantes : {u['tentatives_restantes']}")

                if u["tentatives_restantes"] <= 0:
                    u["locked_until"] = time.time() + BLOCAGE
                    u["tentatives_restantes"] = 3
                    print("Compte verrouillé pendant 15 minutes.")

                sauvegarder_utilisateurs(utilisateurs)
                return None, None, None

    print("Login ou mot de passe incorrect.")
    return None, None, None
