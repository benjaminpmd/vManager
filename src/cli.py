"""
This file contain the main function to run.
This class

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

# importing modules needed for the CLI to run correctly
from ics.ics_manager import ICSManager
from vcf.vcf_manager import VCFManager
from vcf.vcard import VCard


def print_card_content(path: str) -> None:
    """! Function that print the content of a VCF file.
    The VCF file can contain multiple contacts.
    
    @param path the path of the file to explore.
    """
    # initiating the manager that will be used and pass it the path of the file
    manager = VCFManager(path)

    # get the vcard list: the contacts in the folder
    vcards: list[VCard] = manager.get_vcards()

    # for each vcard print data
    for vcard in vcards:
        # basic informations
        print(f"=> {vcard.get_full_name()}")
        print(f"    > Name: {' '.join(vcard.get_names())}")
        
        # print data depending on their existence
        if vcard.get_title() != '':
            print(f"    > Title: {vcard.get_title()}")

        # print data depending on their existence 
        if vcard.get_org() != '':
            print(f"    > Organization: {vcard.get_org()}")
        
        # print each address of the contact
        for address in vcard.get_addresses():
            # check if the address is the preferred one or not
            if (address.is_preferred()):
                print(f"    > Address of types {', '.join(address.get_address_types())}: {' '.join(address.get_address_elements())} (preferred)")
            else:
                print(f"    > Address of types {', '.join(address.get_address_types())}: {' '.join(address.get_address_elements())}")
        
        # print each email of the contact
        for email in vcard.get_emails():
            if (email.is_preferred()):
                # check if the email is the preferred one or not
                print(f"    > Email of types {', '.join(email.get_email_types())}: {email.get_email_address()} (preferred)")
            else:
                print(f"    > Email of types {', '.join(email.get_email_types())}: {email.get_email_address()}")

        # print each phone of the contact
        for phone in vcard.get_phones():
            if (phone.is_preferred()):
                # check if the phone is the preferred one or not
                print(f"    > Phone of types {', '.join(phone.get_phone_types())}: {phone.get_phone_number()} (preferred)")
            else:
                print(f"    > Phone of types {', '.join(phone.get_phone_types())}: {phone.get_phone_number()}")
    
        # end with the note of the user
        if vcard.get_note():
            print(f"    > Note: {vcard.get_note()}")


def print_calendar_content(path: str):
    manager = ICSManager(path)
    for event in manager.get_vevents():
        print("\n=> " + event.get_summary())
        print("     > Creation Date:   " + event.get_timestamp().strftime("%Y-%m-%d %H:%M:%S"))
        print("     > Starting date:   " + event.get_dtstart().strftime("%Y-%m-%d %H:%M:%S"))
        print("     > End date:        " + event.get_dtend().strftime("%Y-%m-%d %H:%M:%S"))
        print("\n")

def export_file(input_path: str, output_path: str):
   
    if input_path.endswith('.vcf'):
        vcf_manager: VCFManager = VCFManager(input_path)
        
        if output_path.endswith('.csv'):
            vcf_manager.export_csv(output_path)
            return "The file has been converted"
        
        elif output_path.endswith('.html'):
            vcf_manager.export_html(output_path)
            return "The file has been converted"
        
        else:
            return "Incorrect file output"
    
    elif input_path.endswith('.ics'):
        ics_manager: ICSManager = ICSManager(input_path)
        
        if output_path.endswith('.csv'):
            ics_manager.export_csv(output_path)
            return "The file has been converted"
        
        elif output_path.endswith('.html'):
            ics_manager.export_html(output_path)
            return "The file has been converted"
        
        else:
            return "Incorrect file output"
    
    else:
        return "Incorrect file input"
            

class CLI:
    def __init__(self, app_name: str, app_version: str) -> None:
        self.__app_name: str = app_name
        self.__app_version: str = app_version

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
                    files[path] = []

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
            files_names = files.get(key)
            if (files_names):
                for value in files_names:
                    print(f"     => {value}")
        print("\n ")

    def print_help(self) -> None:
        """! A function that print help."""

        print(f"Help of {self.__app_name} Version {self.__app_version}\n")
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

    cli: CLI = CLI(config.APP_NAME, config.VERSION)

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
        case 5:
            if (argv[1] == "-i") and (argv[3] == "-h"):
                print(export_file(argv[2], argv[4]))
        case other:
            pass


if __name__ == '__main__':
    main(sys.argv)
