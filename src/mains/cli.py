"""
This file contain the main function to run.

@author Benjamin PAUMARD
@version 0.0.1
@since  2022.04.11
"""

#!/usr/bin/env python

# -*- coding: utf-8 -*-

# importing library to read the parameters passed by the user
import sys

# import constants
import config.constants as constants

def print_help() -> None:
    """! A function that print help."""
    print(f"Help of {constants.APP_NAME} Version {constants.VERSION}\n")
    print("-h or -- help to print help.")
    print("-d '{path}' list all the vci and vcf files present in the specified directory.")
    print("-i '{path}' show the content of a specific vci or vsf file.")
    print("-i '{input path}' -h '{output path}' export a vci or vcf file to html.")
    print("You can also use the graphical version of the application using python.")

def main(argv: list) -> None:
    """! Function executing the script and processing the arguments passed in parameters
    The parameters of the function are passed by the user when running the script.

    @param argv the parameters passed by the user.
    """
    # getting the number of parameters
    # parameters of index 0 will be the call to the script
    argc: int = len(argv)
    # calling the different methods depending of the parameters passed
    match argc:
        case 1:
            # if there is only one argument, then it's the call to the script
            print("It seems you forgot parameters, use -h or --help for more informations.")
        case 2:
            if ((argv[1] == "-h") or (argv[1] == "--help")):
                print_help()
            else:
                print("It seems your parameters are not correct, use -h or --help for more informations.") 
        case 3:
            pass
        case other:
            pass


if __name__ == '__main__':
    main(sys.argv)