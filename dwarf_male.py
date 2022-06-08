import random
import numpy as np 
import pandas as pd

#DWARF MALE

def choose_dwarf_male():
    df_names_dwarf_male = pd.read_excel("npc_data/dwarf_male_names.xls")
    df_weight_dwarf_male = pd.read_excel("npc_data/dwarf_weight.xls")
    df_height_dwarf_male = pd.read_excel("npc_data/dwarf_height.xls")
    df_hair_style_dwarf_male = pd.read_excel("npc_data/hair_styles.xls")
    df_hair_color_dwarf_male = pd.read_excel("npc_data/hair_color.xls")
    df_face_dwarf_male = pd.read_excel("npc_data/face_types.xls")
    df_eye_color_dwarf_male = pd.read_excel("npc_data/eye_color.xls")
    df_tone_dwarf_male = pd.read_excel("npc_data/voice_tones.xls")
    df_skin_tone_dwarf_male = pd.read_excel("npc_data/skin_tones.xls")

    r_name_dwarf_male = df_names_dwarf_male.sample(1)
    r_weight_dwarf_male = df_weight_dwarf_male.sample(1)
    r_height_dwarf_male = df_height_dwarf_male.sample(1)
    r_hair_style_dwarf_male = df_hair_style_dwarf_male.sample(1)
    r_hair_color_dwarf_male = df_hair_color_dwarf_male.sample(1)
    r_face_dwarf_male = df_face_dwarf_male.sample(1)
    r_eye_color_dwarf_male = df_eye_color_dwarf_male.sample(1)
    r_tone_dwarf_male = df_tone_dwarf_male.sample(1)
    r_skin_dwarf_male = df_skin_tone_dwarf_male.sample(1)

    dwarf_male_dict1 = { "Race": "Dwarf",
                    "Sex": "Male",
                    "Name": r_name_dwarf_male.iloc[0,0], 
                    "Height": r_height_dwarf_male.iloc[0,0],
                    "Weight": r_weight_dwarf_male.iloc[0,0],
                    "Hair Style": r_hair_style_dwarf_male.iloc[0,0],
                    "Hair Color": r_hair_color_dwarf_male.iloc[0,0],
                    "Face": r_face_dwarf_male.iloc[0,0],
                    "Eye Color": r_eye_color_dwarf_male.iloc[0,0],
                    "Skin Tone": r_skin_dwarf_male.iloc[0,0],
                    "Voice Tone": r_tone_dwarf_male.iloc[0,0],
                    }
    return dwarf_male_dict1