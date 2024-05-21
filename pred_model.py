import pickle
import os
import numpy as np
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))



    

def pred_diabet_model(data):
    
    return diabetes_model.predict([data])


def pred_heart_disease(data):

    return heart_disease_model.predict([data])


def pred_parkinsons(data):

    return parkinsons_model.predict([data])

def pred_any(data):
    pass

