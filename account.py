import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('movie-recommendation-sys-56c49-45d603070f48.json')
# firebase_admin.initialize_app(cred)

def app():
    st.title('Movie Recommendation System')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def authentication():
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            
            global Username
            Username=(user.uid)
            
            st.session_state.signedout = True
            st.session_state.signout = True  
        except:
            st.error('Login Failed')

    def signout():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''

    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False    

    if not st.session_state['signedout']:

        choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if choice == 'Login':
            st.button('Login', on_click=authentication)

        else:
            username = st.text_input('Enter Username')

            if st.button('Create my account'):
                user = auth.create_user(email = email, password = password, uid = username)
                st.success('Account created successfully')
                st.markdown('Please Login with your email and password')
                st.balloons()

    if st.session_state.signout:
        st.text('Hello '+ st.session_state.username)
        st.button('Sign Out', on_click=signout)