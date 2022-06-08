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
        properties_label = Label(root, text = row + ":")
        properties_label.grid(row=index + 1, column=0, pady=10)
        

#Generate funciton
def generate():
        
        global npc
        if sex_choice.get() == "Male":
                if race_choice.get() == "Dwarf":
                        npc = choose_dwarf_male()
                elif race_choice.get() == "Elf":
                        npc = choose_elf_male()
                elif race_choice.get() == "Gnome":
                        npc = choose_gnome_male()
                elif race_choice.get() == "Halfling":
                        npc = choose_halfling_male()
                elif race_choice.get() == "Human":
                        npc = choose_human_male()
        elif sex_choice.get() == "Female":
                if race_choice.get() == "Dwarf":
                        npc = choose_dwarf_female()
                elif race_choice.get() == "Elf":
                        npc = choose_elf_female()
                elif race_choice.get() == "Gnome":
                        npc = choose_gnome_female()
                elif race_choice.get() == "Halfling":
                        npc = choose_halfling_female()
                elif race_choice.get() == "Human":
                        npc = choose_human_female()
        else:
                npc = {}

        for w in details_label:
                w.destroy()

        details_label.clear()

        for index,(key, value) in enumerate(npc.items()):
                details_label.append(Label(root, text=value, font=("Aerial 10")))
                details_label[-1].grid(row=index+1, column=1, pady=10)
   
#Choose Sex of NPC
sex_options = ["Male", "Female"]
sex_choice = StringVar()
sex_choice.set("Choose Sex")
#Choose Race of NPC
race_options = ["Dwarf", "Elf", "Gnome", "Halfling", "Human"]
race_choice = StringVar()
race_choice.set("Choose Race")
#Sex dropdown menu
sex_dropdown_menu = OptionMenu(root, sex_choice, *sex_options)
sex_dropdown_menu.grid(row=0, column=0, pady=15, padx=5)
#Race dropdown menu
race_dropdown_menu = OptionMenu(root, race_choice, *race_options).grid(row=0, column=1, pady=15, padx=5)

#Generate NPC Button
generate_button = Button(root, text="Generate NPC", command=generate).grid(row=0, column=2, pady=15, padx=5)

root.mainloop()