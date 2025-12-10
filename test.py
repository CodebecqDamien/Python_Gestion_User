import string
import random
import hashlib

def generer_pwd():
    while True:
        try:
            taille = int(input("Choisir le nombre de caractères du mot de passe (minimum 10): "))
            if taille >= 10:
                break
            print("La taille minimale est de 10 caractères.\n")
        except ValueError:
            print("Veuillez entrer un nombre valide.\n")

    chars = string.ascii_letters + string.digits + "!@#$%^&*"

    # Génération du mot de passe
    pwd = "".join(random.choice(chars) for _ in range(taille))

    # Hachage
    pwd_hash = hashlib.sha256(pwd.encode()).hexdigest()

    return pwd, pwd_hash

if __name__ == "__main__":
    mot_de_passe, mot_de_passe_hache = generer_pwd()
    print(f"Mot de passe généré : {mot_de_passe}")
    print(f"Mot de passe haché : {mot_de_passe_hache}")