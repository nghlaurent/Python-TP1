# Python - TP1
Ceci est un TP pour apprendre à installer Python, VScode et Git


## Python

Avant de commencer, il faut avoir Python, qui doit être installer sur l'ordinateur.


### Installation du logiciel

- Sous Windows
	Télécharger la dernière version : ``https://www.python.org/downloads/``

- Sous Ubuntu/Debian
	``sudo apt install python3``


### Installation d'un environnement virtuel en Python

Un environnement virtuel est une arborescence de dossiers qui contiens les fichiers exécutables Python et autres fichiers qui indiquent que c'est un environnement virtuel.

- Création d'un virtualenv
	``sudo apt install python3``
	S'il y a une erreur : ``sudo apt install python3-venv``

- Activation de l'environnement
	◉ ``my_env\Scripts\activate.ps1`` (sous Windows)

	◉ ``source my_env/bin/activate`` (sous Ubuntu/Debian)

- Installation des modules
	◉ ``pip install -r requirements.txt`` (quand on a clone un projet)

	◉ ``pip install -e .`` (quand on est dans le projet)

	◉ ``pip install 'mon_module'``

_exemple_: Executez la commande ``telnet mapscii.me`` pour commencer ensuite [...]


## VScode

L'un des outils le plus important de VScode est la capacité de déboguer les applications directement sur l'éditeur sans même avoir recours aux navigateurs, grâce à un système de points d'arrêt et une console de débogage intégrée qui permet de résoudre les problèmes directement dans l'éditeur.

- Télécharger _VSCode_
	``https://code.visualstudio.com/``

- Dans les extensions, installer le plugin _Python_


## Git

Git permet à différentes versions d'un même fichier de coexister. Les développeurs travaillant avec Git ont accès à l'historique des modifications pour l'intégralité du projet et peuvent ainsi savoir quels changements ont été fait par rapport à leur version des fichiers, qui a fait ces changements, etc.

- Installation de _git_
	◉ ``https://git-scm.com/downloads`` (sous Windows)

	◉ ``sudo apt install git`` (sous Ubuntu/Debian)


### Commandes git en cli / sur VScode

- Création d'un dépot _git_
	``git init``

- Ajout d'un dépot distant
	``git remote add origin link_du_git``

- Clone du dépot distant
	``git clone <i>link_du_git</i>``

- Pull du dépot distant
	``git pull origin master``

- Commit
	``git commit -m "message"``

- Push du dépot local
	``git push origin master``


## License

Ce projet est temporaire, car il s'agit d'apprendre les bases.