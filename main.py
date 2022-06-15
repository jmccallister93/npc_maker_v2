import imp
import random
import numpy as np 
import pandas as pd
import os
import tkinter
import customtkinter
from pandastable import Table, TableModel, config
from tkinter import *
from dwarf_female import *
from dwarf_male import *
from elf_female import *   
from elf_male import *
from gnome_female import *
from gnome_male import * 
from halfling_female import *
from halfling_male import *
from human_female import *
from human_male import *

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
root = customtkinter.CTk()
root.title("NPC Maker")
root.geometry("300x725")

#Define details label
details_label = []
npc = {}

#Set NPC Properties list
npc_properties = ["Race",
                "Sex",
                "Name", 
                "Height",
                "Weight",
                "Hair Style",
                "Hair Color",
                "Face",
                "Eye Color",
                "Skin Tone",
                "Voice Tone"]

#Print NPC properties as row headers
for index, row in enumerate(npc_properties):
        properties_label = customtkinter.CTkLabel(root, text = row + ":")
        properties_label.grid(row=index + 2, column=0, pady=10)
        

#Generate funciton
def generate():
        
        global npc
        sex_choice = StringVar()
        sex_choice = sex_dropdown_menu.get()
        race_choice = StringVar()
        race_choice = race_dropdown_menu.get()

        if  sex_choice == "Male":
                if race_choice == "Dwarf":
                        npc = choose_dwarf_male()
                elif race_choice == "Elf":
                        npc = choose_elf_male()
                elif race_choice == "Gnome":
                        npc = choose_gnome_male()
                elif race_choice == "Halfling":
                        npc = choose_halfling_male()
                elif race_choice == "Human":
                        npc = choose_human_male()
        elif sex_choice == "Female":
                if race_choice == "Dwarf":
                        npc = choose_dwarf_female()
                elif race_choice == "Elf":
                        npc = choose_elf_female()
                elif race_choice == "Gnome":
                        npc = choose_gnome_female()
                elif race_choice == "Halfling":
                        npc = choose_halfling_female()
                elif race_choice == "Human":
                        npc = choose_human_female()
        else:
                npc = {}

        for w in details_label:
                w.destroy()

        details_label.clear()

        for index,(key, value) in enumerate(npc.items()):
                details_label.append(customtkinter.CTkLabel(root, text=value))
                details_label[-1].grid(row=index+2, column=1, pady=10)

        
        

#Sex/Race Options
sex_options = ["Male", "Female"]
race_options = ["Dwarf", "Elf", "Gnome", "Halfling", "Human"]

#Sex Dropdown Menu
sex_dropdown_menu = customtkinter.CTkComboBox(root, values=sex_options)
sex_dropdown_menu.grid(row=1, column=0, pady=15, padx=5)
sex_dropdown_menu.set("Choose Sex")

#Race Dropdown Menu
race_dropdown_menu = customtkinter.CTkComboBox(root, values=race_options)
race_dropdown_menu.grid(row=1, column=1, pady=15, padx=5)
race_dropdown_menu.set("Choose Race")

#Generate NPC Button
generate_button = customtkinter.CTkButton(root, text="Generate NPC", command=generate)
generate_button.grid(row=0, column=0, columnspan=2, pady=15, padx=5)

#Save function
def save_npc():
        as_save=[]
        for key,value in npc.items():
                as_save.append(f"{key}: {value}")
              
        file_naming = npc["Name"]
        file = open(f"npc_{file_naming}.txt", "w")
        file.write(str(as_save))
        file.close



#Save NPC Button
save_button = customtkinter.CTkButton(root, text="Save NPC", command=save_npc)
save_button.grid(row=14, column=0, columnspan=2, pady=15, padx=5)


root.mainloop()