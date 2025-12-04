## ��� Console de Gestion du Système d'Information

Ce système propose une interface en ligne de commande pour la gestion des utilisateurs et des ressources système.

### Menu Principal ���

| N° | Fonctionnalité | Rôle (Tâche) |
| :--- | :--- | :--- |
| **1** | **Gestion des Utilisateurs** | T1 |
| **2** | **Gestion des Fichiers (STF)** | T2 |
| **3** | **Gestion FTP/Réseau** | T3 |
| **0** | **Quitter l'application** | |

---

### Rôles et Droits d'Accès ���️

| Rôle | Description | Périmètre de Gestion |
| :--- | :--- | :--- |
| **SuperAdmin** | Rôle le plus élevé. Gère la création des **Administrateurs** et interagit avec l'**Active Directory (AD)**. | Tous les sites et l'infrastructure globale. |
| **Administrateur** | Gère les utilisateurs. Les droits sont basés sur le site d'affectation. | **Strictement limité à son site** (ex : Marseille, Rennes, Grenoble). |
| **User** | Utilisateur standard (non-admin). | Services et ressources standard. |

> ⚠️ **Note Importante :** Chaque Administrateur est restreint. Un Admin de Marseille ne peut ni gérer, ni consulter les utilisateurs ou ressources de Rennes ou Grenoble.

---

### Authentification de l'Utilisateur (Admin/SuperAdmin) ���

* **Identifiants :**
    * **Login :** `tjacques` (exemple)
    * **Mot de passe :** `xxxxxx` (saisi de manière masquée, ex. via `getpass`)

* **Sécurité :**
    * En cas d'échec de la connexion après **3 tentatives**, l'utilisateur est considéré comme une menace potentielle de **force brute**.
    * Le compte doit être **bloqué** (verrouillé) pour une durée de **15 minutes**.

---

### Menu de Gestion des Utilisateurs (T1) ���

| N° | Action | Détails et Enregistrement |
| :--- | :--- | :--- |
| **1.1** | **Création d'un Utilisateur** | Saisie des informations de base (Nom, Prénom, Mail). Génération automatique du Login et du Mot de passe. **Choix du Profil :** `admin` (avec spécification du site : Marseille, Rennes, Grenoble) ou `user` (autre). **Sauvegarde** des données dans une structure persistante (Liste/Dictionnaire en TP, puis CSV ou BDD). |
| **1.2** | **Modification d'un Utilisateur** | Mise à jour des informations existantes (Mail, Profil, etc.). |
| **1.3** | **Suppression d'un Utilisateur** | Suppression définitive du compte. |
| **1.4** | **Consultation des Utilisateurs** | Affichage de la liste complète, consultation d'un utilisateur **spécifique**, ou filtrage par **type de profil** (Admin/User) ou par site. |
| **1.0** | **Retour au Menu Principal** | |

---

### ��� Prochaines Étapes de TP (Travaux Pratiques)

* Implémenter la **structure de données** (liste et dictionnaire) pour la gestion initiale des utilisateurs avant le passage à un format persistant (CSV/BDD).
* Se concentrer sur la **logique d'authentification** et la **gestion des erreurs/blocages** (point 3 échecs).
