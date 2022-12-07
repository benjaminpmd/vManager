"""! File that contain the GUI.
The GUI allow to open an ICS or VCF file and modify it.

@author Benjamin PAUMARD
@version 1.0.0
@since 05 December 2022
"""

import os

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox

from config import config

from manager.vcf_manager import VCFManager
from manager.ics_manager import ICSManager

class GUIHelp(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

    def run(self) -> None:
        self.mainloop()

class GUI(tk.Tk):
    """! Class that contains the GUI.
    This GUI features an ICS/VCF viewer and editor.
    
    @author Benjamin PAUMARD
    @version 1.0.0
    @since 05 December 2022
    """
    def __init__(self) -> None:
        """! Constructor of the GUI class"""
        # init super
        super().__init__()

        # set the colors
        self.__fg_color: str = "white"
        self.__bg_color: str = "#171e28"
        self.__panel_color: str = "#2e3c50"
        
        # create the menus
        self.__menubar: tk.Menu = tk.Menu(self)
        self.__file_menu: tk.Menu = tk.Menu(self.__menubar, tearoff=0)
        self.__help_menu: tk.Menu = tk.Menu(self.__menubar, tearoff=0)

        # title
        self.__title: tk.Label = tk.Label(self, text=config.APP_NAME, background=self.__bg_color, foreground=self.__fg_color, font=("Arial", 20))
        self.__opened_file_name: tk.Label = tk.Label(self, text="No opened file", background=self.__bg_color, foreground=self.__fg_color, font=("Arial", 15))

        # file management
        # file type opened
        self.__filetype: str = ''
        # managers
        self.__vcf: VCFManager = VCFManager()
        self.__ics: ICSManager = ICSManager()

        self.init()


    def init(self) -> None:
        """! Method that init the GUI."""

        # set the file
        self.title(f"{config.APP_NAME} {config.VERSION}")

        # configure background
        self.configure(bg=self.__bg_color)

        # config geometry
        self.geometry(f"{config.WIDTH}x{config.HEIGHT}")

        # add the menu to the config
        self.config(menu=self.__menubar)
        
        # add options to the file menu commands
        self.__file_menu.add_command(label="Open", command=self.open_file)
        self.__file_menu.add_command(label="Save", command=self.save_file)
        self.__file_menu.add_command(label="Save as...", command=self.save_as_file)
        self.__file_menu.add_command(label="Close", command=self.destroy)
        # add the file menu to the main menu
        self.__menubar.add_cascade(label="File", menu=self.__file_menu)

        # add options to the help menu commands
        self.__help_menu.add_command(label="About", command=self.run_help)
        # add the help menu to the main menu
        self.__menubar.add_cascade(label="Help", menu=self.__help_menu)
    
        # labels
        self.__title.pack()
        self.__opened_file_name.pack()

    def save_file(self) -> None:
        """! Saves a file as requested by the user.
        A file name will be asked to the user.
        """
        # if is a VCF, then use the vcf manager
        if (self.__filetype == 'vcf'):
            self.__vcf.save()
        
        # else its an ICS use the ICS manager
        elif (self.__filetype == 'ics'):
            self.__ics.save()

    def save_as_file(self) -> None:
        """! Saves a file as requested by the user.
        A file name will be asked to the user.
        """
        
        # set the files types to use
        filetypes: tuple = (
            ('Calendar files', '*.ics'),
            ('Card files', '*.vcf')
        )

        # ask for the filename
        filename: str = fd.asksaveasfilename(filetypes=filetypes, initialdir=os.getcwd(),)
        
        # if is a VCF, then use the vcf manager
        if (self.__filetype == 'vcf'):
            self.__vcf.save(f"{filename}.vcf")
        
        # else its an ICS use the ICS manager
        elif (self.__filetype == 'ics'):
            self.__ics.save(f"{filename}.ics")

    def open_file(self) -> None:
        """! Open a file."""

        # set the files types to use
        filetypes = (
            ('Calendar files', '*.ics'),
            ('Card files', '*.vcf')
        )
        
        # ask for the filename
        filename = fd.askopenfilename(filetypes=filetypes, initialdir=os.getcwd())
        
        if (filename == ''):
            return

        # if is a VCF, then use the vcf manager
        elif (filename.endswith('.vcf') or filename.endswith('.VCF')):
            try:
                self.__vcf.read(filename)
                self.__filetype = 'vcf'
            except:
                messagebox.showinfo(f"Corrupted file - {config.APP_NAME}", "The file you are trying to open cannot be read by the application.")
                return

        # else its an ICS use the ICS manager
        elif (filename.endswith('.ics') or filename.endswith('.ICS')):
            try:
                self.__ics.read(filename)
                self.__filetype = 'ics'
            except:
                messagebox.showinfo(f"Corrupted file - {config.APP_NAME}", "The file you are trying to open cannot be read by the application.")
                return

        else:
            messagebox.showinfo(f"Incorrect file - {config.APP_NAME}", "The file you are trying to open is not supported by the application.")
            return

        temp: str = ''
        for char in filename[::-1]:
                # if the char is ; or : append a new element
                if (char == '/') or (char == '\\'):
                    self.__opened_file_name["text"] = temp[::-1]
                    return
                else:
                    # else append the element to the last string in the element list
                    temp = f"{temp}{char}"

    def run_help(self) -> None:
        GUIHelp().run()

    def run(self) -> None:
        """! method that run the GUI."""
        self.mainloop()


if __name__ == '__main__':
    GUI().run()