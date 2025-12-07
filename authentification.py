from gestion_users import charger_utilisateurs
import time

BLOCAGE = 15 * 60  # 15 minutes en secondes

def connexion_admin():
    utilisateurs = charger_utilisateurs()
    login = input("Login admin : ")
    pwd = input("Password : ")

    for u in utilisateurs:
        if u["login"] == login and u["role"] == "admin":

            # Vérification blocage
            if u["locked_until"] and time.time() < u["locked_until"]:
                reste = int((u["locked_until"] - time.time()) // 60)
                print(f"Compte verrouillé. Réessayez dans {reste} min.")
                return None, None

            # Vérification mot de passe
            if u["password"] == pwd:
                u["tentatives_restantes"] = 3
                return u["login"], u["site"]
            else:
                u["tentatives_restantes"] -= 1
                print(f"Mot de passe incorrect. Tentatives restantes : {u['tentatives_restantes']}")
                if u["tentatives_restantes"] <= 0:
                    u["locked_until"] = time.time() + BLOCAGE
                    u["tentatives_restantes"] = 3
                    print("Compte verrouillé pendant 15 minutes.")
                return None, None

    print("Login ou mot de passe incorrect.")
    return None, None
