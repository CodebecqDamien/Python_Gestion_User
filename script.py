from auth import authentification
from menu import menu_principal

if __name__ == "__main__":
    user = authentification()
    if user:
        menu_principal()
    else:
        print("Fermeture du programme.")
