import streamlit as st

st.markdown('## Montagne')
st.markdown('### Site sur les montagnes')

# Champ de saisie
user_input = st.text_input("Quel est votre nom ?")

if st.button("Cliquer ici") == True:
    # Affichage
    st.write("Bonjour " + user_input)

with st.form("My form"):
    user_name = st.text_input("Quel est votre nom ?")

    age = st.slider("Quel est votre age", 18, 100, 35)

    if st.form_submit_button('Envoyer'):
        st.write("Bonjour " + user_name + 'tu as ' + str(age))

if st.sidebar.checkbox("Montrer l'image"):
    st.sidebar.image("mountain.jpg")

col1, col2 = st.columns(2)

with col1:
    st.image("mountain.jpg")

with col2:
    st.video("https://www.youtube.com/watch?v=TgIokghVsUs")