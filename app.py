import history, query, home, account
import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Movie Recommendation"
)

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_apps(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run():

        with st.sidebar:
            app = option_menu(
                menu_title="Recommender",
                options=["Home","Queries","History","Account"],
                menu_icon=['film'],
                icons=['house-fill','collection', 'search', 'person-circle'],
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'#020403'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#40e0d0"},
        "nav-link-selected": {"background-color": "#02ab21"},}
            )

        if app == 'Home':
            home.app()
        if app == 'Queries':
            query.app()
        if app == 'History':
            history.app()
        if app == 'Account':
            account.app()
    
    run()

# firebase = pyrebase.initialize_app(firebaseConfig)
# auth = firebase.auth()

# db = firebase.database()
# storage = firebase.storage()

# st.sidebar.title("Movie Reccommendor")

# choice = st.sidebar.selectbox('login/Signup',['Login', 'Sign Up'])

# email = st.sidebar.text_input("Please enter your email address")
# password = st.sidebar.text_input('Please enter your password', type='password')

# if choice == 'Sign Up':
#     handle = st.sidebar.text_input('Please input your username',value='Default')
#     submit = st.sidebar.button('Create my account')

#     if submit:
#         user = auth.create_user_with_email_and_password(email, password)
#         st.success('Your account is created successfully!!!')
#         st.balloons()

#         user = auth.sign_in_with_email_and_password(email, password)
#         print(handle)
#         # db.child(user['localId']).child('Handle').set(handle)
#         # db.child(user['localId']).child('ID').set(user['localId'])
#         # db.child("users").child("ID").set(user['localId'], user["idToken"])
#         # db.child("users").child("Handle").set(handle, user["idToken"])
#         st.title('Welcome ' + handle)

# if choice == 'Login':
#     login = st.sidebar.checkbox('Login')
#     if login:
#         user = auth.sign_in_with_email_and_password(email,password)

# with st.sidebar:
#     selected = option_menu(
#         menu_title="Recommender",
#         options=["Search","Queries"],
#         menu_icon=['film'],
#         icons=['search-heart','collection']
#     )

# st.title("Movie Recommendation System")

# if selected == "Search":
#     st.title(f"{selected}")
# if selected == "Queries":
#     row_input = st.columns((1,1,1))
#     with row_input[0]:
#         actor_1 = st.text_input("Actor 1",key="Actor 1",max_chars=20)
#     with row_input[1]:
#         actor_2 = st.text_input("Actor 2",key="Actor 2",max_chars=20)
#     with row_input[2]:
#         director = st.text_input("Director",key="Director",max_chars=20)
#     genre = st.text_input("Genre",key="Genre",max_chars=20)
#     desc = st.text_area("Description",max_chars=50)
#     submit_button = st.button("Submit", type='primary')

# # if selected == "Friends":
# #     st.title(f"{selected}")