## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

---

## Déploiement

**Pré-requis :**

- Un compte/acces Github
- Un compte/acces CircleCi
- Un Compte/acces DockerHub
- Un Compte/Acces Heroku

### Pipeline CircleCi

#### Pour le commit sur une branche autre que master :

- lance le workflow 'commit_on_other_branch' qui éxecute le job 'build-and-test':
    - lance les tests via pytest
    - contrôle le linting PEP8 via Flake8

#### Pour le commit sur la branche master : 

- le workflow commit_on_master va se lancer :
     - le job 'build-and-test' qui :
        - lance les tests via pytest,
        - contrôle le linting PEP8 via Flake8,
     - le job 'build-and-push-on-docker' :   
        - qui crée l'image docker et l'upload sur le docker hub et le push,
     - le job 'deploy' :      
        - lance le build sur heroku via Git et le déploie.

## Github :

[Github Repository](https://github.com/FraPar/P-13_OC_Lettings) permet de faire le versionning de notre projet/application.

## CircleCi :

Afin d'utiliser correctement CircleCI, il vous faudra :
Créer les variables d'environnement au niveau du projet :
  - Dans **Projets**, cliquez sur le menu de votre projet,
  - Cliquez sur `Project Settings`
  - Cliquez sur `Environment Variables`  
  - Cliquez sur `Add Environment Variables`  


|   Nom des Variables  |   Description   |   Valeurs à renseigner   |
|---    |---   |---    |
|   DOCKER_USER   |   User Docker Hub   |   `frapar`   |
|   DOCKER_TOKEN   |   Token Dockerhub ou Mdp   |   `62900a8f-2c57-40c7-a31f-4f18c9ea6216`   |
| HEROKU_APP_NAME | Le nom de l'application | oc-lettings-777 |
|   HEROKU_API_KEY |  API Token Heroku  |   `443503a9-39d0-45a4-ba3b-51821d2d9345`   |

## Docker Hub :

[Docker-Hub frapar Repository](https://hub.docker.com/repository/docker/frapar/p-13_oc_lettings) permet de stocker en ligne l'image docker de notre application.  

- Nom de l'application : p13-oc-lettings
- Compte Hub Docker : frapar

## Heroku :

[L'application sur Heroku](https://oc-lettings-777.herokuapp.com/)  

Heroku permet d'heberger notre application.
En cas de necessité ou en cas de suppression, il faut créer l'application 'oc-lettings-777'.  
