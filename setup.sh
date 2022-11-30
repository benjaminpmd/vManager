#!/bin/bash

# function to setup the environment
setup() {
    echo "===================================================================="
    echo "If any error occur, please run: 'sudo apt update && sudo apt upgrade'"
    echo ""
    echo "This script requiere Python 3, venv and pip, tkinter make sure their are installed."
    echo "=> To install them, type: 'sudo apt install python3 python3-venv python3-pip python3-tk'"
    echo "===================================================================="
    echo ""

    echo "Setting up server environment, it may take some time (~1min)..."
    python3 -m venv venv

    echo ""
    echo "Activating server environment..."
    source ./venv/bin/activate

    echo ""
    echo "Installing librairies..."
    pip install -r requierements.txt

    echo ""
    echo "===================================================================="
    echo "To run the server, remember to activate the paython environement" 
    echo "by using: 'source ./venv/bin/activate'"
    echo "===================================================================="
}

setup
