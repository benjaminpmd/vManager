"""! File that contain the GUI.
The GUI allow to open an ICS or VCF file and modify it.

@author Benjamin PAUMARD
@version 1.0.0
@since 05 December 2022
"""

# !/usr/bin/env python

# -*- coding: utf-8 -*-

from datetime import datetime
import os

import tkinter as tk
from tkinter import filedialog as fd
from tkinter import messagebox

from config import config

from process.manager.vcf_manager import VCFManager
from process.manager.ics_manager import ICSManager

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
        self.__frame_bg_color: str = "#2e3c50"
        self.__entry_bg_color: str = "#4e5558"
        self.__button_bg_color: str = "#1d4ed8"
        
        # create the menus
        self.__menubar: tk.Menu = tk.Menu(self)
        self.__file_menu: tk.Menu = tk.Menu(self.__menubar, tearoff=0)

        # title
        self.__title_label: tk.Label = tk.Label(self, text=config.APP_NAME, background=self.__bg_color, foreground=self.__fg_color, font=("Arial", 20))
        self.__opened_filename_label: tk.Label = tk.Label(self, text="No opened file", background=self.__bg_color, foreground=self.__fg_color, font=("Arial", 15))
        self.__credits_label: tk.Label = tk.Label(self, text=f"{config.APP_NAME} | Version: {config.VERSION} | Project made at CYU University | Author: Benjamin PAUMARD", background=self.__bg_color, foreground=self.__fg_color, font=("Arial", 10))
        
        # main frame
        self.__work_frame: tk.Frame = tk.Frame(self, background=self.__bg_color, width=config.WIDTH, height=config.HEIGHT-90)

        # set sub frames
        self.__view_frame: tk.Frame = tk.Frame(self.__work_frame, background=self.__frame_bg_color, width=(config.WIDTH//2)-10, height=(config.HEIGHT-95))
        self.__edit_frame: tk.Frame = tk.Frame(self.__work_frame, background=self.__frame_bg_color, width=(config.WIDTH//2)-10, height=(config.HEIGHT-95))

        # scrollbar
        self.__scrollbar: tk.Scrollbar = tk.Scrollbar(self.__view_frame)

        # element list
        self.__list_view: tk.Text = tk.Text(self.__view_frame, yscrollcommand=self.__scrollbar.set, background=self.__frame_bg_color, foreground=self.__fg_color, borderwidth=0, highlightthickness=0, state="disabled", font=("sans-serif", 12))

        # VCARD EDIT ELEMENTS
        # labels
        self.__vcard_full_name_label: tk.Label = tk.Label(self.__edit_frame, text="Full Name", background=self.__bg_color, foreground=self.__fg_color)
        self.__vcard_title_label: tk.Label = tk.Label(self.__edit_frame, text="Title", background=self.__bg_color, foreground=self.__fg_color)
        self.__vcard_org_label: tk.Label = tk.Label(self.__edit_frame, text="Organization", background=self.__bg_color, foreground=self.__fg_color)
        self.__vcard_names_label: tk.Label = tk.Label(self.__edit_frame, text="Names", background=self.__bg_color, foreground=self.__fg_color)
        # entries
        self.__vcard_full_name_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vcard_title_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vcard_org_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vcard_names_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        # buttons
        self.__vcard_save_button: tk.Button = tk.Button(self.__edit_frame, text="Save", padx=10, pady=10, background=self.__button_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__return_button: tk.Button = tk.Button(self.__edit_frame, text="Save", padx=10, pady=10, background=self.__button_bg_color, foreground=self.__fg_color, highlightthickness=0, command=self.set_selection_edit_frame)
   
        # VEVENTS EDIT ELEMENTS
        # labels
        self.__vevent_summary_label: tk.Label = tk.Label(self.__edit_frame, text="Summary", background=self.__bg_color, foreground=self.__fg_color)
        self.__vevent_dtstart_label: tk.Label = tk.Label(self.__edit_frame, text="Starting date", background=self.__bg_color, foreground=self.__fg_color)
        self.__vevent_dtend_label: tk.Label = tk.Label(self.__edit_frame, text="Ending date", background=self.__bg_color, foreground=self.__fg_color)
        self.__vevent_location_label: tk.Label = tk.Label(self.__edit_frame, text="Location", background=self.__bg_color, foreground=self.__fg_color)
        # entries
        self.__vevent_summary_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vevent_dtstart_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vevent_dtend_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vevent_location_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        # buttons
        self.__vevent_save_button: tk.Button = tk.Button(self.__edit_frame, text="Save", padx=10, pady=10, background=self.__button_bg_color, foreground=self.__fg_color, highlightthickness=0)
        
        # VTODO EDIT ELEMENTS
        # labels
        self.__vtodo_summary_label: tk.Label = tk.Label(self.__edit_frame, text="Summary", background=self.__bg_color, foreground=self.__fg_color)
        self.__vtodo_dtstart_label: tk.Label = tk.Label(self.__edit_frame, text="Starting date", background=self.__bg_color, foreground=self.__fg_color)
        self.__vtodo_duration_label: tk.Label = tk.Label(self.__edit_frame, text="Duration", background=self.__bg_color, foreground=self.__fg_color)
        self.__vtodo_status_label: tk.Label = tk.Label(self.__edit_frame, text="Status", background=self.__bg_color, foreground=self.__fg_color)
        # entries
        self.__vtodo_summary_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vtodo_dtstart_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vtodo_duration_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vtodo_status_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        # buttons
        self.__vtodo_save_button: tk.Button = tk.Button(self.__edit_frame, text="Save", padx=10, pady=10, background=self.__button_bg_color, foreground=self.__fg_color, highlightthickness=0)
    

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
        self.resizable(False, False)

        # config geometry
        self.geometry(f"{config.WIDTH}x{config.HEIGHT}")

        # add the menu to the config
        self.config(menu=self.__menubar)


        # export menu system
        export_menu: tk.Menu = tk.Menu(self.__file_menu, tearoff=0)
        export_menu.add_command(label="HTML", command=lambda: self.export('html', False))
        export_menu.add_command(label="Full HTML page", command=lambda: self.export('html', True))
        export_menu.add_command(label="CSV", command=lambda: self.export('csv', False))
        
        # add options to the file menu commands
        self.__file_menu.add_command(label="Open", command=self.open_file)
        self.__file_menu.add_command(label="Save", command=self.save_file)
        self.__file_menu.add_command(label="Save as...", command=self.save_as_file)
        self.__file_menu.add_command(label="Import", command=self.import_from_exported_file)
        self.__file_menu.add_cascade(label="Export as", menu=export_menu)
        self.__file_menu.add_command(label="Close", command=self.destroy)
        # add the file menu to the main menu
        self.__menubar.add_cascade(label="File", menu=self.__file_menu)

        # set the list view
        self.__list_view.pack(side="left", fill="both")

        # scrollbar
        self.__scrollbar.pack(side="right", fill="y")
        self.__scrollbar.config(command=self.__list_view.yview)        
    
        self.__edit_frame.pack_propagate(False)
        self.__view_frame.pack_propagate(False)
        self.__view_frame.grid(row=0, column=0, padx=5, pady=5)
        self.__edit_frame.grid(row=0, column=1, padx=5, pady=5)

        # packing to the main window
        self.__title_label.pack()
        self.__opened_filename_label.pack()
        self.__work_frame.pack()
        self.__credits_label.pack()

    def save_file(self) -> None:
        """! Saves a file as requested by the user.
        A file name will be asked to the user.
        """
        if self.__filetype.startswith("export"):
            messagebox.showwarning(f"Cannot save - {config.APP_NAME}", "You are viewing an exported file.")
            return

        # elif is a VCF, then use the vcf manager
        elif (self.__filetype == 'vcf'):
            self.__vcf.save()
        
        # elif its an ICS use the ICS manager
        elif (self.__filetype == 'ics'):
            self.__ics.save()

    def save_as_file(self) -> None:
        """! Saves a file as requested by the user.
        A file name will be asked to the user.
        """

        if self.__filetype.startswith("export"):
            messagebox.showwarning(f"Cannot save - {config.APP_NAME}", "You are viewing an exported file.")
            return
        
        # set the files types to use
        filetypes: tuple = (
            ('HTML files', '*.html'),
            ('CSV files', '*.csv')
        )

        # ask for the filename
        filename: str = fd.asksaveasfilename(filetypes=filetypes, initialdir=os.getcwd())
    
        if filename == '':
            return
        
        # if is a VCF, then use the vcf manager
        if (self.__filetype == 'vcf'):
            if (filename.endswith('.vcf')):
                self.__vcf.save(filename)
            else:
                self.__vcf.save(f"{filename}.vcf")
        
        # else its an ICS use the ICS manager
        elif (self.__filetype == 'ics'):
            if (filename.endswith('.ics')):
                self.__ics.save(filename)
            else:
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
                self.__list_view.config(state='disabled')
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

        self.set_view_frame_content()
        self.set_selection_edit_frame()

        # create the title
        temp: str = ''
        for char in filename[::-1]:
                # if the char is ; or : append a new element
                if (char == '/') or (char == '\\'):
                    self.__opened_filename_label["text"] = f"Editing {temp[::-1]}"
                    return
                else:
                    # else append the element to the last string in the element list
                    temp = f"{temp}{char}"

    def import_from_exported_file(self) -> None:
        """! Import an HTML or CSV file."""
        # set the files types to use
        filetypes = (
            ('HTML files', '*.html'),
            ('CSV', '*.csv')
        )
        
        # ask for the filename
        filename = fd.askopenfilename(filetypes=filetypes, initialdir=os.getcwd())
        
        if (filename == ''):
            return

        export_type: str = ''

        for widget in self.__edit_frame.winfo_children():
            widget.destroy()

        # if is a VCF, then use the vcf manager
        if (filename.endswith('.csv') or filename.endswith('.CSV')):
            
            # check for the type of the exported file
            with open(filename, 'r') as f:
                # read the line
                line: str = f.readline()

                # check if the exported file is vcards or calendar
                if line.startswith("type"):
                    export_type = "ics"
                
                elif line.startswith("full name"):
                    export_type = "vcf"
            
            # if the exported file is a VCF
            if export_type == 'vcf':
                try:
                    self.__vcf.import_from_file(filename)
                    self.__filetype = 'export-vcf'
                except:
                    messagebox.showinfo(f"Corrupted file - {config.APP_NAME}", "The file you are trying to open cannot be read by the application.")

            # else if the exported type is ICS
            elif export_type == 'ics':
                try:
                    self.__ics.import_from_file(filename)
                    self.__filetype = 'export-ics'
                except Exception as e:

                    messagebox.showinfo(f"Corrupted file - {config.APP_NAME}", "The file you are trying to open cannot be read by the application.")

        # else its an ICS use the ICS manager
        elif filename.endswith('.html'):
            with open(filename, 'r') as f:
                line: str = f.readline()
                if line.startswith("<!--vcalendar"):
                    export_type = "ics"
                
                elif line.startswith("<!--vcards"):
                    export_type = "vcf"

            if export_type == 'vcf':
                try:
                    self.__vcf.import_from_file(filename)
                    self.__filetype = 'export-vcf'
                except:
                    messagebox.showinfo(f"Corrupted file - {config.APP_NAME}", "The file you are trying to open cannot be read by the application.")

            elif export_type == 'ics':
                try:
                    self.__ics.import_from_file(filename)
                    self.__filetype = 'export-ics'
                except Exception as e:
                    messagebox.showinfo(f"Corrupted file - {config.APP_NAME}", "The file you are trying to open cannot be read by the application.")
        else:
            messagebox.showinfo(f"Incorrect file - {config.APP_NAME}", "The file you are trying to open is not supported by the application.")

        self.set_view_frame_content()

        # create the title
        temp: str = ''
        for char in filename[::-1]:
                # if the char is ; or : append a new element
                if (char == '/') or (char == '\\'):
                    self.__opened_filename_label["text"] = f"Viewing {temp[::-1]}"
                    return
                else:
                    # else append the element to the last string in the element list
                    temp = f"{temp}{char}"

    def export(self, export_type: str, full_html_page: bool = False) -> None:
        """! Export a file into a HTML microformat or a CSV file.
        This method should be called by the menu.
        
        @param export_type the type to export (HTML or CSV).
        @param full_html_page wether the HTML generated page should use only microformat or complete page rendering.
        """
        
        # set the files types to use
        if self.__filetype.startswith("export"):
            messagebox.showwarning(f"Cannot save - {config.APP_NAME}", "You are viewing an exported file.")
            return

        filetypes = []

        if export_type == 'html':
            filetypes = [("HTML files", "*.html")]

        elif export_type == 'csv':
            filetypes = [("CSV files", "*.csv")]
        

        # ask for the filename
        filename: str = fd.asksaveasfilename(filetypes=filetypes, initialdir=os.getcwd())
    
        if filename == '':
            return
        
        if export_type == 'html':
            # if is a VCF, then use the vcf manager
            if (self.__filetype == 'vcf'):
                
                if (filename.endswith('.html')):
                    self.__vcf.export_html(filename, full_html_page)
                
                else:
                    self.__vcf.export_html(f"{filename}.html", full_html_page)

            # else its an ICS use the ICS manager
            elif (self.__filetype == 'ics'):
                
                if (filename.endswith('.html')):
                    self.__ics.export_html(filename, full_html_page)
                
                else:
                    self.__ics.export_html(f"{filename}.html", full_html_page)

        elif export_type == 'csv':
            # if is a VCF, then use the vcf manager
            if (self.__filetype == 'vcf'):
                
                if (filename.endswith('.csv')):
                    self.__vcf.export_csv(filename)
                
                else:
                    self.__vcf.export_csv(f"{filename}.csv")

            # else its an ICS use the ICS manager
            elif (self.__filetype == 'ics'):
                
                if (filename.endswith('.csv')):
                    self.__ics.export_csv(filename)
                
                else:
                    self.__ics.export_csv(f"{filename}.csv")

    def set_view_frame_content(self) -> None:
        """! Set the content of the view frame."""
        # if is a VCF, then use the vcf manager
        self.__list_view.config(state='normal')
        self.__list_view.delete(0.0, 'end')
        self.__list_view.config(state='disabled')
        
        if (self.__filetype == 'vcf' or self.__filetype == 'export-vcf'):
            for vcard in self.__vcf.get_vcards():
                # for each vcard print data
                # basic informations
                string: str = f"{vcard.get_full_name()}\n"
                string += f"\nName:\n{' '.join(vcard.get_names())}\n"
                
                # print data depending on their existence
                if vcard.get_title() != '':
                    string += f"\nTitle:\n{vcard.get_title()}\n"
            
                # print data depending on their existence 
                if vcard.get_org() != '':
                    string += f"\nOrg:\n{vcard.get_org()}\n"
                
                # print each address of the contact
                string += f"\nAddresses:\n"
                for address in vcard.get_addresses():
                    # check if the address is the preferred one or not
                    if (address.is_preferred()):
                        string += f"{' '.join(address.get_address_elements())} (preferred)\n"
                    else:
                        string += f"{' '.join(address.get_address_elements())}\n"
                
                # print each email of the contact
                string += f"\nEmails:\n"
                for email in vcard.get_emails():
                    if (email.is_preferred()):
                        # check if the email is the preferred one or not
                        string += f"{email.get_email_address()} (preferred)\n"
                    else:
                        string += f"{email.get_email_address()}\n"
            
                # print each phone of the contact
                string += f"\nPhones:\n"
                for phone in vcard.get_phones():
                    if (phone.is_preferred()):
                        # check if the phone is the preferred one or not
                        string += f"{phone.get_phone_number()} (preferred)\n"
                    else:
                        string += f"{phone.get_phone_number()}\n"
            
                # end with the note of the user
                if vcard.get_note():
                    string += f"\nNote:\n{vcard.get_note()}\n\n"
                else:
                    string += "\n"
                
                string += "---------------------------------------\n\n"
                self.__list_view.config(state='normal')
                self.__list_view.insert(tk.END, string)
                self.__list_view.config(state='disabled')

        # else its an ICS use the ICS manager
        elif self.__filetype == 'ics' or self.__filetype == 'export-ics':
            # for each event, print it
            for event in self.__ics.get_vevents():
                string: str = ''
                string += f"{event.get_summary()}\n\n"
                string += f"Creation Date\n{str(event.get_timestamp())}\n\n"
                string += f"Starting date\n{str(event.get_dtstart())}\n\n"
                string += f"End date\n{str(event.get_dtend())}\n\n"
                string += f"Location\n{str(event.get_location())}\n\n"
                string += "---------------------------------------\n\n"
                self.__list_view.config(state='normal')
                self.__list_view.insert(tk.END, string)
                self.__list_view.config(state='disabled')
            
            # for each event, print it
            for todo in self.__ics.get_vtodos():
                string: str = ''
                string += f"{todo.get_summary()}\n\n"
                string += f"Creation Date\n{str(todo.get_timestamp())}\n\n"
                string += f"Starting date\n{str(todo.get_dtstart())}\n\n"
                string += f"Duration\n{str(todo.get_duration())}\n\n"
                string += "---------------------------------------\n\n"
                self.__list_view.config(state='normal')
                self.__list_view.insert(tk.END, string)
                self.__list_view.config(state='disabled')


    def set_selection_edit_frame(self) -> None:
        """! Change the content of the frame to edit data."""
        
        # reset the frame
        for widgets in self.__edit_frame.winfo_children():
            widgets.destroy()

        if (self.__filetype == 'vcf'):
            # scrollbar
            scrollbar: tk.Scrollbar = tk.Scrollbar(self.__edit_frame)
            scrollbar.pack(side="right", fill="y")
            # element list
            list_view: tk.Listbox = tk.Listbox(self.__edit_frame, width=(config.WIDTH//2)-10, yscrollcommand=self.__scrollbar.set, background=self.__frame_bg_color, foreground=self.__fg_color, borderwidth=0, highlightthickness=0)
            # set the list view
            list_view.pack(side="top", fill="both")
            # config the view
            scrollbar.config(command=list_view.yview)
            # set the selections
            for card in self.__vcf.get_vcards():
                list_view.insert(tk.END, card.get_full_name())
            # create the button and pack it
            edit_button: tk.Button = tk.Button(self.__edit_frame, text="Edit", padx=5, pady=5, background=self.__button_bg_color, foreground=self.__fg_color, borderwidth=0, highlightthickness=0, command=lambda: self.set_vcard_edit_frame(list_view, list_view.curselection()))
            edit_button.pack()

        elif (self.__filetype == 'ics'):
            event_frame: tk.Frame = tk.Frame(self.__edit_frame, background=self.__frame_bg_color, width=(config.WIDTH//2)-10, height=10)
            todo_frame: tk.Frame = tk.Frame(self.__edit_frame, background=self.__frame_bg_color, width=(config.WIDTH//2)-10, height=10)
            ############## Part for the event frame
            title_event = tk.Label(event_frame, text="Events", background=self.__frame_bg_color, foreground=self.__fg_color, font=("sans-serif, 13"))
            title_event.pack()

            # create the button and pack it
            edit_button_event: tk.Button = tk.Button(event_frame, text="Edit", padx=20, pady=5, background=self.__button_bg_color, foreground=self.__fg_color, borderwidth=0, highlightthickness=0, command=lambda: self.set_vevent_edit_frame(list_view_event, list_view_event.curselection()))
            edit_button_event.pack()
            # scrollbar
            scrollbar_event: tk.Scrollbar = tk.Scrollbar(event_frame)
            scrollbar_event.pack(side="right", fill="y")
            # element list
            list_view_event: tk.Listbox = tk.Listbox(event_frame, yscrollcommand=self.__scrollbar.set, width=(config.WIDTH//2)-10, height=5, background=self.__frame_bg_color, foreground=self.__fg_color, borderwidth=0, highlightthickness=0)
            # set the list view
            list_view_event.pack()
            # config the view
            scrollbar_event.config(command=list_view_event.yview)
            # set the selections
            for vevents in self.__ics.get_vevents():
                list_view_event.insert(tk.END, vevents.get_summary())
            event_frame.pack()

            ############## Part for the todo frame
            title_todo = tk.Label(todo_frame, text="Todos", background=self.__frame_bg_color, foreground=self.__fg_color, font=("sans-serif, 13"))
            title_todo.pack()
            
            # create the button and pack it
            edit_button_todo: tk.Button = tk.Button(todo_frame, text="Edit", padx=20, pady=5, background=self.__button_bg_color, foreground=self.__fg_color, borderwidth=0, highlightthickness=0, command=lambda: self.set_vtodo_edit_frame(list_view_todo, list_view_todo.curselection()))
            edit_button_todo.pack()
            # scrollbar
            scrollbar_todo: tk.Scrollbar = tk.Scrollbar(todo_frame)
            scrollbar_todo.pack(side="right", fill="y")
            # element list
            list_view_todo: tk.Listbox = tk.Listbox(todo_frame, width=(config.WIDTH//2)-10, height=5, yscrollcommand=self.__scrollbar.set, background=self.__frame_bg_color, foreground=self.__fg_color, borderwidth=0, highlightthickness=0)
            # set the list view
            list_view_todo.pack()
            # config the view
            scrollbar_todo.config(command=list_view_todo.yview)
            # set the selections
            for vtodos in self.__ics.get_vtodos():
                list_view_todo.insert(tk.END, vtodos.get_summary())
            todo_frame.pack()
        
    def set_vcard_edit_frame(self, elements: tk.Listbox,  ids: tuple) -> None:
        """! Change the content of the frame to edit vcard.
        This only affect the edit frame.

        @param elements the complete list of names.
        @param ids a tuple containing the selected ID.
        """
        # reset the frame
        card = self.__vcf.get_vcard_from_name(elements.get(ids[0]))
        if (card is None):
            return

        for widgets in self.__edit_frame.winfo_children():
            widgets.destroy()
        
        self.__vcard_full_name_label = tk.Label(self.__edit_frame, text="Full Name", background=self.__frame_bg_color, foreground=self.__fg_color)
        self.__vcard_title_label: tk.Label = tk.Label(self.__edit_frame, text="Title", background=self.__frame_bg_color, foreground=self.__fg_color)
        self.__vcard_org_label: tk.Label = tk.Label(self.__edit_frame, text="Organization", background=self.__frame_bg_color, foreground=self.__fg_color)
        self.__vcard_names_label: tk.Label = tk.Label(self.__edit_frame, text="Names", background=self.__frame_bg_color, foreground=self.__fg_color)

        self.__vcard_full_name_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vcard_full_name_entry.insert(0, card.get_full_name())
        
        self.__vcard_title_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vcard_title_entry.insert(0, card.get_title())

        self.__vcard_org_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vcard_org_entry.insert(0, card.get_org())

        self.__vcard_names_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vcard_names_entry.insert(0, ' '.join(card.get_names()))

        self.__vcard_save_button: tk.Button = tk.Button(self.__edit_frame, text="Save", padx=20, pady=5, background=self.__button_bg_color, foreground=self.__fg_color, highlightthickness=0, borderwidth=0, command=self.save_vcard)
        self.__return_button: tk.Button = tk.Button(self.__edit_frame, text="Return", padx=20, pady=5, background=self.__button_bg_color, foreground=self.__fg_color, highlightthickness=0, borderwidth=0, command=self.set_selection_edit_frame)
        
        self.__vcard_full_name_label.pack()
        self.__vcard_full_name_entry.pack()
        
        self.__vcard_title_label.pack()
        self.__vcard_title_entry.pack()

        self.__vcard_org_label.pack()
        self.__vcard_org_entry.pack()

        self.__vcard_names_label.pack()
        self.__vcard_names_entry.pack()

        self.__vcard_save_button.pack()
        tk.Label(self.__edit_frame, bg=self.__frame_bg_color).pack()
        self.__return_button.pack()

    def save_vcard(self) -> None:
        """! Method triggered by the save of a vcard."""
        self.__vcf.update_current_card(self.__vcard_full_name_entry.get(), self.__vcard_names_entry.get().split(' '), self.__vcard_org_entry.get(), self.__vcard_title_entry.get())
        self.set_selection_edit_frame()

    def set_vevent_edit_frame(self, elements: tk.Listbox,  ids: tuple) -> None:
        """! Change the content of the frame to edit vcard.
        This only affect the edit frame.

        @param elements the complete list of names.
        @param ids a tuple containing the selected ID.
        """
        # reset the frame
        event = self.__ics.get_event_from_summary(elements.get(ids[0]))
        if (event is None):
            return
        for widgets in self.__edit_frame.winfo_children():
            widgets.destroy()

        # buttons
        self.__vevent_summary_label: tk.Label = tk.Label(self.__edit_frame, text="Summary", background=self.__frame_bg_color, foreground=self.__fg_color)
        self.__vevent_dtstart_label: tk.Label = tk.Label(self.__edit_frame, text="Starting date", background=self.__frame_bg_color, foreground=self.__fg_color)
        self.__vevent_dtend_label: tk.Label = tk.Label(self.__edit_frame, text="Ending date", background=self.__frame_bg_color, foreground=self.__fg_color)
        self.__vevent_location_label: tk.Label = tk.Label(self.__edit_frame, text="Location", background=self.__frame_bg_color, foreground=self.__fg_color)
        
        self.__vevent_summary_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vevent_summary_entry.insert(0, event.get_summary())
        
        self.__vevent_dtstart_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vevent_dtstart_entry.insert(0, str(event.get_dtstart()))

        self.__vevent_dtend_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vevent_dtend_entry.insert(0, str(event.get_dtend()))

        self.__vevent_location_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vevent_location_entry.insert(0, event.get_location())

        self.__vevent_save_button: tk.Button = tk.Button(self.__edit_frame, text="Save", padx=20, pady=5, background=self.__button_bg_color, foreground=self.__fg_color, highlightthickness=0, borderwidth=0, command=self.save_vevent)
        self.__return_button: tk.Button = tk.Button(self.__edit_frame, text="Return", padx=20, pady=5, background=self.__button_bg_color, foreground=self.__fg_color, highlightthickness=0, borderwidth=0, command=self.set_selection_edit_frame)
        
        self.__vevent_summary_label.pack()
        self.__vevent_summary_entry.pack()
        
        self.__vevent_dtstart_label.pack()
        self.__vevent_dtstart_entry.pack()

        self.__vevent_dtend_label.pack()
        self.__vevent_dtend_entry.pack()

        self.__vevent_location_label.pack()
        self.__vevent_location_entry.pack()        

        self.__vevent_save_button.pack()
        tk.Label(self.__edit_frame, bg=self.__frame_bg_color).pack()
        self.__return_button.pack()

    def save_vevent(self) -> None:
        """! Method triggered by the save of a vevent."""
        try:
            self.__ics.update_current_event(self.__vevent_summary_entry.get(), datetime.fromisoformat(self.__vevent_dtstart_entry.get()), datetime.fromisoformat(self.__vevent_dtend_entry.get()), self.__vevent_location_entry.get())
            self.set_selection_edit_frame()
        except:
            messagebox.showwarning(f"{config.APP_NAME}", "Warning, could not convert the dates entered.")

    def set_vtodo_edit_frame(self, elements: tk.Listbox,  ids: tuple) -> None:
        """! Change the content of the frame to edit vcard.
        This only affect the edit frame.

        @param elements the complete list of names.
        @param ids a tuple containing the selected ID.
        """
        # reset the frame
        todo = self.__ics.get_todo_from_summary(elements.get(ids[0]))
        if (todo is None):
            return
        for widgets in self.__edit_frame.winfo_children():
            widgets.destroy()

        # buttons
        self.__vtodo_summary_label: tk.Label = tk.Label(self.__edit_frame, text="Summary", background=self.__frame_bg_color, foreground=self.__fg_color)
        self.__vtodo_dtstart_label: tk.Label = tk.Label(self.__edit_frame, text="Starting date", background=self.__frame_bg_color, foreground=self.__fg_color)
        self.__vtodo_duration_label: tk.Label = tk.Label(self.__edit_frame, text="Duration", background=self.__frame_bg_color, foreground=self.__fg_color)
        self.__vtodo_status_label: tk.Label = tk.Label(self.__edit_frame, text="Status", background=self.__frame_bg_color, foreground=self.__fg_color)
        
        self.__vtodo_summary_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vtodo_summary_entry.insert(0, todo.get_summary())
        
        self.__vtodo_dtstart_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vtodo_dtstart_entry.insert(0, str(todo.get_dtstart()))

        self.__vtodo_duration_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vtodo_duration_entry.insert(0, str(todo.get_duration()))

        self.__vtodo_status_entry: tk.Entry = tk.Entry(self.__edit_frame, width=50, background=self.__entry_bg_color, foreground=self.__fg_color, highlightthickness=0)
        self.__vtodo_status_entry.insert(0, todo.get_status())

        self.__vtodo_save_button: tk.Button = tk.Button(self.__edit_frame, text="Save", padx=20, pady=5, background=self.__button_bg_color, foreground=self.__fg_color, highlightthickness=0, borderwidth=0, command=self.save_vtodo)
        self.__return_button: tk.Button = tk.Button(self.__edit_frame, text="Return", padx=20, pady=5, background=self.__button_bg_color, foreground=self.__fg_color, highlightthickness=0, borderwidth=0, command=self.set_selection_edit_frame)
        
        self.__vtodo_summary_label.pack()
        self.__vtodo_summary_entry.pack()
        
        self.__vtodo_dtstart_label.pack()
        self.__vtodo_dtstart_entry.pack()

        self.__vtodo_duration_label.pack()
        self.__vtodo_duration_entry.pack()

        self.__vtodo_status_label.pack()
        self.__vtodo_status_entry.pack()        

        self.__vtodo_save_button.pack()
        tk.Label(self.__edit_frame, bg=self.__frame_bg_color).pack()
        self.__return_button.pack()

    def save_vtodo(self) -> None:
        """! Method triggered by the save of a vtodo."""
        try:
            self.__ics.update_current_todo(self.__vtodo_summary_entry.get(), datetime.fromisoformat(self.__vtodo_dtstart_entry.get()), self.__vtodo_duration_entry.get(), self.__vtodo_status_entry.get())
            self.set_selection_edit_frame()
        except:
            messagebox.showwarning(f"{config.APP_NAME}", "Warning, could not convert the date entered.")

    def run(self) -> None:
        """! method that run the GUI."""
        self.mainloop()


if __name__ == '__main__':
    GUI().run()