import pandas as pd
import json
import streamlit as st
import streamlit.components.v1 as components
from streamlit_option_menu import option_menu

from pred_model import  pred_heart_disease, pred_diabet_model, pred_parkinsons, pred_symptom, create_copy_button
symptoms = pd.read_csv('symptoms/Symptom-severity.csv')
symptoms['Symptom'] = symptoms['Symptom'].str.replace('_',' ')
symptom_translated = pd.read_csv('symptoms/translated/symptom_translated.csv')
symptom_translated['Symptom'] = symptom_translated['Symptom'].str.replace('_',' ')


# Set page configuration
st.set_page_config(page_title="پیشبینی بیماری",
                   layout="wide",
                   page_icon="🩺⚕")

    

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',

                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Symptom Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'bi-heart-pulse', 'person', 'bi-clipboard-pulse'],
                           styles={
                                        "container": {"padding": "0!important", "background-color": "#000000"},
                                        "icon": {"color": "red", "font-size": "28px"}, 
                                        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#bbbbbb"},
                                        "nav-link-selected": {"background-color": "gray"},
                                  },
                           default_index=0)

    
# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # persian toggle
    on = st.toggle(":flag-ir: :flag-us: Lang", help="toggle languege perosian or english")

    # page title
    st.title('Diabetes Prediction')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)


    if on:
        with col1:
            Pregnancies = st.text_input('تعداد بارداری‌ها')

        with col2:
            Glucose = st.text_input('سطح گلوکز')

        with col3:
            BloodPressure = st.text_input('فشار خون')

        with col1:
            SkinThickness = st.text_input('ضخامت پوست')

        with col2:
            Insulin = st.text_input('سطح انسولین')

        with col3:
            BMI = st.text_input('شاخص توده بدنی')

        with col1:
            DiabetesPedigreeFunction = st.text_input('ضریب وراثت دیابت')

        with col2:
            Age = st.text_input('سن فرد')
    else:
        with col1:
            Pregnancies = st.text_input('Number of Pregnancies')

        with col2:
            Glucose = st.text_input('Glucose Level')

        with col3:
            BloodPressure = st.text_input('Blood Pressure value')

        with col1:
            SkinThickness = st.text_input('Skin Thickness value')

        with col2:
            Insulin = st.text_input('Insulin Level')

        with col3:
            BMI = st.text_input('BMI value')

        with col1:
            DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

        with col2:
            Age = st.text_input('Age of the Person')


    # code for Prediction
    diab_diagnosis = ''
######################################################################################
        #                  #
        #   DEVELOP CODER  #
        #       START      #
    def predmulti():
        # از این روش استفاده میکنم چون دارم استرینگ دسته ای میدم نه از فرم
        st.info(st.session_state.name)
        # input_list = st.session_state.name.split(", ")
        l1 = st.session_state.name.split(',')
        list1 = [float(x) for x in l1]#[:8]
        list2 = list1[:8]
        
        multi_pred = pred_diabet_model(list2)
        if multi_pred[0] == 1:
            pred_diabet = 'The person is diabetic❌'
        else:
            pred_diabet = 'The person is not diabetic✔'

        real_pred_diabet = int(list1[8])
        if multi_pred[0] == real_pred_diabet:
            st.success(pred_diabet+str(list1[8]))
        else:
            st.error(pred_diabet+str(list1[8]))
        

    with st.form(key="my_form"):
        st.text_input("Multiple input here:", key="name")
        st.form_submit_button("SUBMIM", on_click=predmulti)
        #                  #
        #   DEVELOP CODER  #
        #        END       #
######################################################################################
    # creating a button for Prediction
    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        if any(x is None or x == '' for x in user_input):
            st.error("All fields must be filled out")
        else:
            user_input = [float(x) for x in user_input]
            diab_prediction = pred_diabet_model(user_input)


            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'

            st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    on = st.toggle(":flag-ir: :flag-us: Lang", help="toggle languege perosian or english")

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    
    if on:
        with col1:
            age = st.text_input('سن')

        with col2:
            sex = st.text_input('جنسیت')

        with col3:
            cp = st.text_input('انواع درد قفسه سینه')

        with col1:
            trestbps = st.text_input('فشار خون استراحت')

        with col2:
            chol = st.text_input('کلسترول سرم در mg/dl')

        with col3:
            fbs = st.text_input('قند خون ناشتا > 120 mg/dl')

        with col1:
            restecg = st.text_input('نتایج الکتروکاردیوگرافی استراحت')

        with col2:
            thalach = st.text_input('حداکثر ضربان قلب به دست آمده')

        with col3:
            exang = st.text_input('آنژین ناشی از ورزش')

        with col1:
            oldpeak = st.text_input('افسردگی ST ناشی از ورزش')

        with col2:
            slope = st.text_input('شیب بخش ST در اوج ورزش')

        with col3:
            ca = st.text_input('رگ‌های اصلی رنگ شده توسط فلوروسکوپی')

        with col1:
            thal = st.text_input('0 = طبیعی; 1 = نقص ثابت; 2 = نقص برگشت پذیر')
    else:
        with col1:
            age = st.text_input('Age')

        with col2:
            sex = st.text_input('Gender')

        with col3:
            cp = st.text_input('Chest Pain types')

        with col1:
            trestbps = st.text_input('Resting Blood Pressure')

        with col2:
            chol = st.text_input('Serum Cholestoral in mg/dl')

        with col3:
            fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

        with col1:
            restecg = st.text_input('Resting Electrocardiographic results')

        with col2:
            thalach = st.text_input('Maximum Heart Rate achieved')

        with col3:
            exang = st.text_input('Exercise Induced Angina')

        with col1:
            oldpeak = st.text_input('ST depression induced by exercise')

        with col2:
            slope = st.text_input('Slope of the peak exercise ST segment')

        with col3:
            ca = st.text_input('Major vessels colored by flourosopy')

        with col1:
            thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = pred_heart_disease(user_input)

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = pred_parkinsons(user_input)

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

#  symptom's Prediction Page
if selected == 'Symptom Prediction':

    # page title
    st.title('Symptom Prediction')

    st.subheader('Please enter your symptoms or medical issues below:')
    # getting the input data from the user
    options = list(symptoms['Symptom']) + list(symptom_translated['translated'])
    
    colE1, colE2, colE3= st.columns([1, 1, 1])
    with colE1:
        englishSym = st.selectbox(
            "persian",
            symptom_translated['translated'],
            index=None,
            placeholder="persian symtom...",
            )
    with colE2:
        if 'english_symptom' not in st.session_state:
            st.session_state['english_symptom'] = ""

        st.text("english")
        if englishSym:
            condition = symptom_translated['translated'] == englishSym
            st.session_state['english_symptom'] = symptom_translated.loc[condition, 'Symptom'].iloc[0]

            st.markdown(f"<h2 style='font-size:28px;padding:0px;margin:0px'>•{st.session_state['english_symptom']}</h2>", unsafe_allow_html=True)


    col1, col2, col3 = st.columns(3)
    with col1:
        symptom1 = st.selectbox(
            'symptom 1',
            options,
            index=None,
            placeholder="input the symptom number 1",
            )


    with col2:
        symptom2 = st.selectbox(
            'symptom 2',
            symptoms,
            index=None,
            placeholder="input the symptom number 2",
            )

    with col3:
        symptom3 = st.selectbox(
            'symptom 3',
            symptoms,
            index=None,
            placeholder="input the symptom number 3",
            )

    with col1:
        symptom4 = st.selectbox(
            'symptom 4',
            symptoms,
            index=None,
            placeholder="input the symptom number 4",
            )

    with col2:
        symptom5 = st.selectbox(
            'symptom 5',
            symptoms,
            index=None,
            placeholder="input the symptom number 5",
            )

    with col3:
        symptom6 = st.selectbox(
            'symptom 6',
            symptoms,
            index=None,
            placeholder="input the symptom number 6",
            )

    with col1:
        symptom7 = st.selectbox(
            'symptom 7',
            symptoms,
            index=None,
            placeholder="input the symptom number 7",
            )

    with col2:
        symptom8 = st.selectbox(
            'symptom 8',
            symptoms,
            index=None,
            placeholder="input the symptom number 8",
            )

    with col3:
        symptom9 = st.selectbox(
            'symptom 9',
            symptoms,
            index=None,
            placeholder="input the symptom number 9",
            )

    # code for Prediction
    symptom_diagnosis = ''
    symptom_prediction = ''
    selected_page = ''
    dicOut = ''
    disease = ''
    description = ''
    precautions = ''
    # creating a button for Prediction    
    if st.button("Symptom's Test Result"):

        user_input = [symptom1, symptom2, symptom3, symptom4, symptom5, symptom6, symptom7, symptom8, symptom9,'','','','','','','','' ]

        # انجام میشود pred_model عملیات پیش پردازش در فایل
        # user_input = [float(x) for x in user_input]

        disease, description, precautions, riskLvl = pred_symptom(user_input)

        if symptom_prediction:
            symptom_diagnosis = f"{symptom_prediction}"
        else:
            symptom_diagnosis = "The person does not have Parkinson's disease"
        
        st.header(":mask: Predicted Disease")
        # st.subheader(disease)


        # CSS import code 

        with open('styles.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

        st.markdown(
            f'<h2 class="{riskLvl}">{disease}</h2>',
            unsafe_allow_html=True
        )

        st.subheader('', divider='rainbow')
        st.header(":memo: Disease Description :+1:")
        st.write(description)
        st.subheader('', divider="rainbow")
        st.header(":pill: Medical Precautions")
        for precaution in precautions:
            st.markdown(f"<h2 style='font-size:24px;'>• {precaution}</h2>", unsafe_allow_html=True)
        
      