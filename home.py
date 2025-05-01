import streamlit as st

st.markdown('## Montagne')
st.markdown('### Site sur les montagnes')

col1, col2 = st.columns(2)

with col1:
    st.image("mountain.jpg")

with col2:
    st.video("https://www.youtube.com/watch?v=TgIokghVsUs")