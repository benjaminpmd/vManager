# vManager

## Description

This project is carried out for the 3rd year of computer license at CY Cergy Paris University. The objective of the latter is the design and production of a vcf and ics file reader. The application works in two ways, the first in the command line allows you to view and export a contact book or a calendar. The second version with a graphical interface offers the same options as the first, but also the possibility of modifying contacts and calendar items as well as viewing exported files.

## Features

Through the two versions of the application, we can find the functionalities. The command line app version has fewer options than the GUI version.

### CLI version

Here are the features offered by the command line version:

- Listing `VCF`/`ICS` files in a directory

- Reading `VCF`/`ICS` files

- Export of `VCF`/`ICS` files in `HTML` and `CSV` formats

It is possible to choose between two export modes for HTML files, the first simply exporting the data using microformats, the second generating a complete HTML page.

### GUI version

Here are the features offered by the Graphical Interface version:

- Reading `VCF`/`ICS` files

- Editing `VCF`/`ICS` files

- Import of HTML/CSS files exported by the application

- Export of `VCF`/`ICS` files in `HTML` and `CSV` formats

Just like the command line version, the graphical version offers two modes for exporting an HTML file, the first by simply exporting the data in HTML format using microformats, the second by exporting the same information, but in a complete HTML page.

## Installation

> This project requires Python 3.10 or higher.

This application uses the `Tkinter` library to produce a graphical display. Check that this library is installed on your machine. This library is installed by default on windows, but not on Linux or MacOS. In this case, you can install it as follows:

```sh


# install Tkinter on Debian or Debian based Linux distro

apt install python3-tk

# install Tkinter on MacOS

brew install tkinter

# or use you own package installer based on your OS
```

## Use

The operation of the application differs depending on the version used. Here below are the different uses of the versions of the application.

### CLI version

In order to launch the application, it is necessary to call the corresponding script as follows: `python3 src/cli.py` (use `python src/cli.py` on Windows). We then place the arguments according to what we want to achieve:

- `-h` or `--help` provides help

- `-d path/to/directory` allows to view `VCF`/`ICS` files in a directory

- `-i path/to/file` allows to view the contents of a file.

- `-i path/to/input_file -c path/to/output_file` allows to export a file in `CSV` format.

- `-i path/to/input_file -h path/to/output_file` allows to export a file in `HTML` format.

- `-i path/to/input_file -h path/to/output_file -p` allows you to export a file in `HTML` format by generating a complete page.

### GUI version

The GUI version is launched by calling the dedicated script like this: `python3 src/gui.py` (use `python src/gui.py` on Windows)
