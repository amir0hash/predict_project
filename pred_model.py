import pickle
import os
import numpy as np
import pandas as pd
import streamlit as st
working_dir = os.path.dirname(os.path.abspath(__file__))
diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

symptom_model = pickle.load(open(f'{working_dir}/saved_models/skops-iw9h_jza.pkl', 'rb'))
ektra7at = pd.read_csv("symptoms/symptom_precaution.csv")

# وزن هر علامت
df1 = pd.read_csv('symptoms/Symptom-severity.csv') 
df1['Symptom'] = df1['Symptom'].str.replace('_',' ')
# توضیهات یک بیماری به بیمار برای کمک
discrp = pd.read_csv("symptoms/symptom_Description.csv")
# دیتاست میزان خطر بیماری
RiskLvlDS = pd.read_csv("symptoms/Disease_Risk_Levels.csv")
# توصیه های پزشکی
tosiye = pd.read_csv("symptoms/symptom_precaution.csv")
teosiye_farsi = pd.read_csv("symptoms/symptom_precaution.csv")

def convert_to_zero_if_empty_or_none(value):
    if value is None or value == '':
        return 0
    return value
def pred_diabet_model(data):
    
    return diabetes_model.predict([data])


def pred_heart_disease(data):

    return heart_disease_model.predict([data])


def pred_parkinsons(data):

    return parkinsons_model.predict([data])


def pred_symptom(data):

    # return data
    data = [convert_to_zero_if_empty_or_none(x) for x in data]

    # return type(data[1])


    psymptoms = data

    a = np.array(df1["Symptom"])
    b = np.array(df1["weight"])
    for j in range(len(psymptoms)):
        for k in range(len(a)):
            if psymptoms[j]==a[k]:
                psymptoms[j]=b[k]

    psy = [psymptoms]
    # عملیات پردینک با الگوریتم جنگل تصادفی
    pred2 = symptom_model.predict(psy)

    # تایین خطر بیماری
    riskLvl = RiskLvlDS[RiskLvlDS['Disease']==pred2[0]]
    riskLvl = riskLvl['Risk Level']
    riskLvl = RiskLvlDS[RiskLvlDS['Disease'] == pred2[0]]['Risk Level'].values[0]
    
    if riskLvl == 1:
        riskLvl = "subheader-red"
    elif riskLvl == 2:
        riskLvl = "subheader-blue"
    elif riskLvl == 3:
        riskLvl = "subheader-yellow"
    elif riskLvl == 4:
        riskLvl = "subheader-green"
    else:
        riskLvl = "subheader-default"

    # توضیحات بیماری
    disp= discrp[discrp['Disease']==pred2[0]]
    disp = disp.values[0][1]
    recomnd = ektra7at[ektra7at['Disease']==pred2[0]]
    c=np.where(ektra7at['Disease']==pred2[0])[0][0]
    precuation_list=[]
    for i in range(1,len(ektra7at.iloc[c])):
          precuation_list.append(ektra7at.iloc[c,i])
    print("The Disease Name: ",pred2[0])
    print("The Disease Discription: ",disp)
    print("Recommended Things to do at home: ")
    for i in precuation_list:
        print(i)
    return pred2[0],disp,precuation_list,riskLvl


def create_copy_button(text_to_copy):
    button_id = "copyButton" + text_to_copy
    
    button_html = f"""<button id="{button_id}">Copy</button>
    <script>
    document.getElementById("{button_id}").onclick = function() {{
        navigator.clipboard.writeText("{text_to_copy}").then(function() {{
            console.log('Async: Copying to clipboard was successful!');
        }}, function(err) {{
            console.error('Async: Could not copy text: ', err);
        }});
    }}
    </script>"""
    
    st.markdown(button_html, unsafe_allow_html=True)