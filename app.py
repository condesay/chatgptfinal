import streamlit as st
import openai


#HELLO WORLD COCO

st.title('Bienvenue - Service OpenAI - Technologie du SI by YLI/PDU')

with st.sidebar:
  st.title('Paramétrages:')
  choix_modeles=st.radio('Modèles',['Davinci'])
  if choix_modeles == 'Ada':
    modele_option=st.selectbox('Mod',['NOT IMPLEMENTED','NOT IMPLEMENTED'])
  if choix_modeles == 'Babbage':
    modele_option=st.selectbox('Mod',['NOT IMPLEMENTED','NOT IMPLEMENTED'])
  if choix_modeles == 'Curie':
    modele_option=st.selectbox('Mod',['NOT IMPLEMENTED','NOT IMPLEMENTED'])
  if choix_modeles == 'Davinci':
    modele_option=st.selectbox('Mod',['Code','Text'])
    if (modele_option=='Code'):
      modele_a_charger="de-code-davinci-002"
    if (modele_option=='Text'):
      modele_a_charger="de-text-davinci-002"

  vtemperature = st.slider('Temperature :', value=0.7,min_value=0., max_value=1., step=.1)
  vtoken= st.slider('Token :', value=190,min_value=0, max_value=2048, step=1)
  vtop=st.slider('Top_p :', value=1.0,min_value=0.0, max_value=1.0, step=.1)
  vfreq_penalty=st.slider('frequence penalty :', value=0.0,min_value=0.0, max_value=1.0, step=.1)
  vpres_penalty=st.slider('Presence penalty :', value=0.0, min_value=0.0, max_value=1.0, step=.1)


txtInput1=st.text_area('Code à Analyser', value="### Postgres SQL tables, with their properties:\n#\n# Employee(id, name, department_id)\n# Department(id, name, address)\n# Salary_Payments(id, employee_id, amount, date)\n#\n### A query to list the names of the departments which employed more than 10 employees in the last 3 months\n\nSELECT",height=300)
txtInputAPPKEY = st.text_input('appKey',value="Appkey")

openai.api_key =txtInputAPPKEY


if st.button("Action"):
  response = openai.Completion.create(
    engine=modele_a_charger,
    prompt=txtInput1,
    temperature=vtemperature,
    max_tokens=vtoken,
    top_p=vtop,
    frequency_penalty=vfreq_penalty,
    presence_penalty=vpres_penalty,
    stop=["YOUYOU:"])
  st.code(response.choices[0].text)
  with st.expander("Debug:",expanded=False):
    st.code(response)



 
