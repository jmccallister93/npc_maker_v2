import random
import numpy as np 
import pandas as pd

#HUMAN FEMALE

def choose_human_female():
    df_names_human_female = pd.read_excel("npc_data/human_female_first_names.xls")
    df_weight_human_female = pd.read_excel("npc_data/human_weight.xls")
    df_height_human_female = pd.read_excel("npc_data/human_height.xls")
    df_hair_style_human_female = pd.read_excel("npc_data/hair_styles.xls")
    df_hair_human_female = pd.read_excel("npc_data/hair_color.xls")
    df_face_human_female = pd.read_excel("npc_data/face_types.xls")
    df_eye_color_human_female = pd.read_excel("npc_data/eye_color.xls")
    df_tone_human_female = pd.read_excel("npc_data/voice_tones.xls")
    df_skin_tone_human_female = pd.read_excel("npc_data/skin_tones.xls")


    r_name_human_female = df_names_human_female.sample(1)
    r_weight_human_female = df_weight_human_female.sample(1)
    r_height_human_female = df_height_human_female.sample(1)
    r_hair_style_human_female = df_hair_style_human_female.sample(1)
    r_hair_human_female = df_hair_human_female.sample(1)
    r_face_human_female = df_face_human_female.sample(1)
    r_eye_color_human_female = df_eye_color_human_female.sample(1)
    r_tone_human_female = df_tone_human_female.sample(1)
    r_skin_human_female = df_skin_tone_human_female.sample(1)

    human_female_dict1 = { "Race": "Human",
                        "Sex": "Female",
                        "Name": r_name_human_female.iloc[0,0], 
                        "Height": r_height_human_female.iloc[0,0],
                        "Weight": r_weight_human_female.iloc[0,0],
                        "Hair Style": r_hair_style_human_female.iloc[0,0],
                        "Hair Color": r_hair_human_female.iloc[0,0],
                        "Face": r_face_human_female.iloc[0,0],
                        "Eye Color": r_eye_color_human_female.iloc[0,0],
                        "Skin Tone": r_skin_human_female.iloc[0,0],
                        "Voice Tone": r_tone_human_female.iloc[0,0],
                    }
    return human_female_dict1