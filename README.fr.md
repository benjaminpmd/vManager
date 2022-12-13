# vManager

## Description

Ce projet est réalisé dans le cadre de la 3e année de licence informatique à CY Cergy Paris Université. L'objectif de ce dernier est la conception et la réalisation d'un lecteur de fichier vcf et ics. L'application fonctionne de deux manières, la première en ligne de commande permet de visualiser et d'exporter un carnet de contact ou un calendrier. La seconde version dotée d'une interface graphique propose les mêmes options que la première, mais également la possibilité de modifier les contacts et éléments du calendrier ainsi que la visualisation des fichiers exportés.

## Fonctionnalités

Au travers des deux versions de l'application, on peut retrouver devers les fonctionnalités. La version de l'application en ligne de commande propose moins d'options que la version utilisant une interface graphique.

### Version CLI

Voici les fonctionnalités proposées par la version en ligne de commande :

- Référencement des fichiers `VCF`/`ICS` dans un répertoire

- Lecture de fichiers `VCF`/`ICS`

- Export de fichiers `VCF`/`ICS` aux formats `HTML` et `CSV`

Il est possible de choisir entre deux modes d'export pour les fichiers HTML, le premier exportant simplement les données en utilisant les microformats, le second générant une page HTML complète.

### Version GUI

Voici les fonctionnalités proposées par la version Interface Graphique :

- Lecture de fichiers `VCF`/`ICS`

- Modification de fichiers `VCF`/`ICS`

- Import de fichiers HTML/CSS exporté par l'application

- Export de fichiers `VCF`/`ICS` aux formats `HTML` et `CSV`

Tout comme la version en ligne de commandes, la version graphique propose deux modes d'export d'un fichier HTML, le premier en exportant simplement les données au format HTML en utilisant les microformats, le second, en exportant les mêmes informations, mais dans une page HTML complète.

## Installation

> Ce projet requière Python 3.10 ou supérieur.

Cette application utilise la librairie `Tkinter` afin de produire un affichage graphique. Vérifiez que cette librairie est bien installée sur votre machine. Cette librairie est installée par défaut sur windows, mais pas sur Linux ou MacOS. Dans ce cas, vous pouvez l'installer de la manière suivante :

```sh


# installer Tkinter sur Debian ou sur une distribution Linux basée sur Debian

apt install python3-tk

# installer Tkinter sur MacOS

brew install tkinter

# ou bien utilisez votre propre installateur de paquets
```

## Utilisation

Le fonctionnement de l'application diffère selon la version utilisée. Voici ci-dessous les différentes utilisations des versions de l'application.

### Version CLI

Afin de lancer l'application, il est nécessaire d'appeler le script correspondant de la manière suivante : `python3 src/cli.py` (utilisez `python src/cli.py` sur Windows). On y place ensuite les arguments en fonction de ce que l'on souhaite réaliser :

- `-h` ou `--help` permet d'obtenir de l'aide

- `-d path/to/directory` permet de visualiser les fichiers `VCF`/`ICS` dans un répertoire

- `-i path/to/file` permet de visualiser le contenu d'un fichier.

- `-i path/to/input_file -c path/to/output_file` permet d'exporter un fichier au format `CSV`.

- `-i path/to/input_file -h path/to/output_file` permet d'exporter un fichier au format `HTML`.

- `-i path/to/input_file -h path/to/output_file -p` permet d'exporter un fichier au format `HTML` en générant une page complète.

### Version GUI

La version GUI se lance en appelant le script dédié comme ceci : `python3 src/gui.py` (utilisez `python src/gui.py` sur Windows)
