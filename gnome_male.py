import random
import numpy as np 
import pandas as pd

#GNOME MALE

def choose_gnome_male():
    df_names_gnome_male = pd.read_excel("npc_data/gnome_male_names.xls")
    df_weight_gnome_male = pd.read_excel("npc_data/gnome_weight.xls")
    df_height_gnome_male = pd.read_excel("npc_data/gnome_height.xls")
    df_hair_style_gnome_male = pd.read_excel("npc_data/hair_styles.xls")
    df_hair_color_gnome_male = pd.read_excel("npc_data/hair_color.xls")
    df_face_gnome_male = pd.read_excel("npc_data/face_types.xls")
    df_eye_color_gnome_male = pd.read_excel("npc_data/eye_color.xls")
    df_tone_gnome_male = pd.read_excel("npc_data/voice_tones.xls")
    df_skin_tone_gnome_male = pd.read_excel("npc_data/skin_tones.xls")

    r_name_gnome_male = df_names_gnome_male.sample(1)
    r_weight_gnome_male = df_weight_gnome_male.sample(1)
    r_height_gnome_male = df_height_gnome_male.sample(1)
    r_hair_style_gnome_male = df_hair_style_gnome_male.sample(1)
    r_hair_color_gnome_male = df_hair_color_gnome_male.sample(1)
    r_face_gnome_male = df_face_gnome_male.sample(1)
    r_eye_color_gnome_male = df_eye_color_gnome_male.sample(1)
    r_tone_gnome_male = df_tone_gnome_male.sample(1)
    r_skin_gnome_male = df_skin_tone_gnome_male.sample(1)

    gnome_male_dict1 = { "Race": "Gnome",
                    "Sex": "Male",
                    "Name": r_name_gnome_male.iloc[0,0], 
                    "Height": r_height_gnome_male.iloc[0,0],
                    "Weight": r_weight_gnome_male.iloc[0,0],
                    "Hair Style": r_hair_style_gnome_male.iloc[0,0],
                    "Hair Color": r_hair_color_gnome_male.iloc[0,0],
                    "Face": r_face_gnome_male.iloc[0,0],
                    "Eye Color": r_eye_color_gnome_male.iloc[0,0],
                    "Skin Tone": r_skin_gnome_male.iloc[0,0],
                    "Voice Tone": r_tone_gnome_male.iloc[0,0],
                    }
    return gnome_male_dict1