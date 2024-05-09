import streamlit as st
from firebase_admin import firestore


db = firestore.client()
st.session_state.db = db

def app():
    st.title('Movie Recommendation System')

    if 'username' in st.session_state and st.session_state["signedout"] == True:

        info = db.collection('History').document(st.session_state.username).get()
        if info.exists:
            history = info.to_dict()['Content']
            history.reverse()
            st.write("Title: \n")
            for title in history:
                st.write("----  " + title)
        else:
            st.warning('No Search History')

    else:
        st.warning('Please Login/SignUp to view Search History')