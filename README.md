# Gestionnaire d'événements

Réalisation : Benjamin P.

## Installation

> Ce projet requière Python 3.10 ou supérieur.

Cette application utilise la librairie `Tkinter` afin de produire un affichage graphique. Vérifiez que cette librairie est bien installée sur votre machine. Cette librairie est installée par défaut sur windows mais pas sur Linux ou MacOS. Dans ce cas, vous pouvez l'installer de la manière suivante :

```sh
# installer Tkinter sur Linux ou MacOS
sudo apt install python3-tk
```

### Librairies

Ce projet requière l'utilisation des librairies tierces suivantes :

- [ics](https://pypi.org/project/ics/)
- [pycvf](https://pypi.org/project/pycvf/)

### Installation manuelle

Pour installer ces librairies manuellement, il est possible d'utiliser l'outil `pip` en installant les librairies de la manière suivante :

```sh
# installer pip sur Linux ou MacOS
sudo apt install python3-pip

# installer les librairies (tout OS confondus)
pip install pyvcf ics
```

### Installation automatisée

Afin de simplifier l'installation et l'utilisation du logiciel, il est possible d'installer les libraires et mettre en place un environnement python de manière automatisé. Pour se faire, deux scripts sont disponibles selon votre OS :

- Linux/MacOS : `./setup.sh`
- Windows : `setup.bat`

Une fois installé, pour executer l'application, il vous faudra activé l’environnement python mit en place :

- Linux/MacOS : `source ./venv/bin/activate`
- Windows :
  - Cmd : `venv\Scripts\activate.bat`
  - Powershell : `venv\Scripts\activate.ps1`

## Execution
