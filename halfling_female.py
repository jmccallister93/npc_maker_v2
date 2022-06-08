import random
import numpy as np 
import pandas as pd

#HALFING FEMALE

def choose_halfling_female():
  df_names_halfing_female = pd.read_excel("npc_data/halfing_female_names.xls")
  df_weight_halfing_female = pd.read_excel("npc_data/halfing_weight.xls")
  df_height_halfing_female = pd.read_excel("npc_data/halfing_height.xls")
  df_hair_style_halfing_female = pd.read_excel("npc_data/hair_styles.xls")
  df_hair_color_halfing_female = pd.read_excel("npc_data/hair_color.xls")
  df_face_halfing_female = pd.read_excel("npc_data/face_types.xls")
  df_eye_color_halfing_female = pd.read_excel("npc_data/eye_color.xls")
  df_tone_halfing_female = pd.read_excel("npc_data/voice_tones.xls")
  df_skin_tone_halfing_female = pd.read_excel("npc_data/skin_tones.xls")

  r_name_halfing_female = df_names_halfing_female.sample(1)
  r_weight_halfing_female = df_weight_halfing_female.sample(1)
  r_height_halfing_female = df_height_halfing_female.sample(1)
  r_hair_style_halfing_female = df_hair_style_halfing_female.sample(1)
  r_hair_color_halfing_female = df_hair_color_halfing_female.sample(1)
  r_face_halfing_female = df_face_halfing_female.sample(1)
  r_eye_color_halfing_female = df_eye_color_halfing_female.sample(1)
  r_tone_halfing_female = df_tone_halfing_female.sample(1)
  r_skin_halfing_female = df_skin_tone_halfing_female.sample(1)

  halfing_female_dict1 = { "Race": "Halfing",
                    "Sex": "Female",
                    "Name": r_name_halfing_female.iloc[0,0], 
                    "Height": r_height_halfing_female.iloc[0,0],
                    "Weight": r_weight_halfing_female.iloc[0,0],
                    "Hair Style": r_hair_style_halfing_female.iloc[0,0],
                    "Hair Color": r_hair_color_halfing_female.iloc[0,0],
                    "Face": r_face_halfing_female.iloc[0,0],
                    "Eye Color": r_eye_color_halfing_female.iloc[0,0],
                    "Skin Tone": r_skin_halfing_female.iloc[0,0],
                    "Voice Tone": r_tone_halfing_female.iloc[0,0],
                  }
  return halfing_female_dict1