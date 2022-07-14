import streamlit as st

st.title('Moje prvni appka')

st.write('Toto je moje prvni aplikace, kterou delam delam.')


page = st.sidebar.radio('Select page',['Test','Thomson'])

if page == 'Test':
    st.write('Toto je moje prvni aplikace, kterou delam delam. Dalsi radky budou super COOL!')

if page == 'Thomson':
    st.write('Thomson sampling')
