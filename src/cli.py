"""
This file contain the main function to run.

@author Benjamin PAUMARD
@version 1.0.0
@since  2022.04.11
"""

# !/usr/bin/env python

# -*- coding: utf-8 -*-

import os
# importing library to read the parameters passed by the user
import sys

# import constants
import config.config as config
from manager.calendar_manager import CalendarManager
from vcard.vcard_manager import VCardManager


def print_card_content(path: str):
    manager = VCardManager(path)
    print(manager.get_vcard())
    # for event in manager.get_formatted_events():
    #    print("\n=> " + event["summary"])
    #    print("     > Date:            " + str(event["timestamp"]))
    #    print("     > Starting date:   " + str(event["start_date"]))
    #    print("     > End date:        " + str(event["end_date"]))
    #    print("     > Creation date:   " + str(event["creation_date"]))
    #    if (event["modified_date"]):
    #        print("     >" + str(event["modified_date"]))
    #    print("     > Repeats " + (' '.join(event["rule"]["repeat"])) + ", ends on " + str(event["rule"]["UNTIL"]))
    #    print("\n")


def print_calendar_content(path: str):
    manager = CalendarManager(path)
    for event in manager.get_formatted_events():
        print("\n=> " + event["summary"])
        print("     > Date:            " + str(event["timestamp"]))
        print("     > Starting date:   " + str(event["start_date"]))
        print("     > End date:        " + str(event["end_date"]))
        print("     > Creation date:   " + str(event["creation_date"]))
        if event["modified_date"]:
            print("     >" + str(event["modified_date"]))
        print("     > Repeats " + (' '.join(event["rule"]["repeat"])) + ", ends on " + str(event["rule"]["until"]))
        print("\n")


class Cli:
    def __init__(self, app_name: str, app_version: str) -> None:
        self.app_name: str = app_name
        self.app_version: str = app_version

    def dir_explorer(self, path: str, files: dict[str, list[str]] = {}) -> dict[str, list[str]]:
        """! Method that list all the .ics and all .vcf files present in a given directory.

        @param path the path of the directory to explore.
        @param files the optional dictionary to use to store listed files.
            It should not be given when calling the function.
        @return a dictionary of files with their parent
        directory as key.
        """

        # fetch the content of the directory
        content: list[str] = os.listdir(path)

        # for each item in the directory
        for item in content:

            # get the relative path of the item
            item_path: str = os.path.join(path, item)

            # if this is a file, and it ends with .ics or .vcf
            if os.path.isfile(item_path) and (item_path.endswith(".ics") or item_path.endswith(".vcf")):

                # creating an entry in the dictionary with the path if it does not exist
                if files.get(path) is None:
                    files[path]: list[str] = []

                # append the file to the list
                files[path].append(item)

            # else if the folder is a directory, then we call recursively the function to get the new dictionary
            elif os.path.isdir(item_path):
                files = self.dir_explorer(item_path, files)

        # return all the files
        return files

    def print_dir_explorer(self, path: str) -> None:
        """! Method that format the output of the dir_explorer function for display in the cli.

        @param path the path to pass to the dir_explorer function (the path to explore).
        """
        # get the files explored by the method
        files: dict = self.dir_explorer(path)

        # for each key (directory path)
        for key in files.keys():
            print(f"\n{key}:")

            # print each file
            for value in files.get(key):
                print(f"     => {value}")
        print("\n ")

    def print_help(self) -> None:
        """! A function that print help."""

        print(f"Help of {self.app_name} Version {self.app_version}\n")
        print("-h or -- help to print help.")
        print(
            "-d '{path}' list all the vci and vcf files present in the specified directory.")
        print("-i '{path}' show the content of a specific vci or vsf file.")
        print(
            "-i '{input path}' -h '{output path}' export a vci or vcf file to html.")
        print("You can also use the graphical version of the application using python.")


def main(argv: list) -> None:
    """! Function executing the script and processing the arguments passed in parameters
    The parameters of the function are passed by the user when running the script.
    @param argv the parameters passed by the user.
    """

    cli: Cli = Cli(config.APP_NAME, config.VERSION)

    # getting the number of parameters
    #  of index 0 will be the call to the script
    argc: int = len(argv)

    # calling the different methods depending on the parameters passed
    match argc:
        case 1:
            # if there is only one argument, then it's the call to the script
            print(
                "It seems you forgot parameters, use -h or --help for more information's.")
        case 2:
            if (argv[1] == "-h") or (argv[1] == "--help"):
                cli.print_help()
            else:
                print(
                    "It seems your parameters are not correct, use -h or --help for more informations.")
        case 3:
            if argv[1] == "-d":
                cli.print_dir_explorer(argv[2])
            elif argv[1] == "-i":

                if argv[2].endswith(".ics"):
                    print_calendar_content(argv[2])

                elif argv[2].endswith(".vcf"):
                    print_card_content(argv[2])

                else:
                    print("Incorrect file input.")
        case other:
            pass


if __name__ == '__main__':
    main(sys.argv)
