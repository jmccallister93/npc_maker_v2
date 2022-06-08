import random
import numpy as np 
import pandas as pd

#ELF FEMALE

def choose_elf_female():
    df_names_elf_female = pd.read_excel("npc_data/elf_female_names.xls")
    df_weight_elf_female = pd.read_excel("npc_data/elf_weight.xls")
    df_height_elf_female = pd.read_excel("npc_data/elf_height.xls")
    df_hair_style_elf_female = pd.read_excel("npc_data/hair_styles.xls")
    df_hair_color_elf_female = pd.read_excel("npc_data/hair_color.xls")
    df_face_elf_female = pd.read_excel("npc_data/face_types.xls")
    df_eye_color_elf_female = pd.read_excel("npc_data/eye_color.xls")
    df_tone_elf_female = pd.read_excel("npc_data/voice_tones.xls")
    df_skin_tone_elf_female = pd.read_excel("npc_data/skin_tones.xls")

    r_name_elf_female = df_names_elf_female.sample(1)
    r_weight_elf_female = df_weight_elf_female.sample(1)
    r_height_elf_female = df_height_elf_female.sample(1)
    r_hair_style_elf_female = df_hair_style_elf_female.sample(1)
    r_hair_color_elf_female = df_hair_color_elf_female.sample(1)
    r_face_elf_female = df_face_elf_female.sample(1)
    r_eye_color_elf_female = df_eye_color_elf_female.sample(1)
    r_tone_elf_female = df_tone_elf_female.sample(1)
    r_skin_elf_female = df_skin_tone_elf_female.sample(1)

    elf_female_dict1 = { "Race": "Elf",
                    "Sex": "Female",
                    "Name": r_name_elf_female.iloc[0,0], 
                    "Height": r_height_elf_female.iloc[0,0],
                    "Weight": r_weight_elf_female.iloc[0,0],
                    "Hair Style": r_hair_style_elf_female.iloc[0,0],
                    "Hair Color": r_hair_color_elf_female.iloc[0,0],
                    "Face": r_face_elf_female.iloc[0,0],
                    "Eye Color": r_eye_color_elf_female.iloc[0,0],
                    "Skin Tone": r_skin_elf_female.iloc[0,0],
                    "Voice Tone": r_tone_elf_female.iloc[0,0],
                    }
    return elf_female_dict1