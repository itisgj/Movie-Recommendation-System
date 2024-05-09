import streamlit as st
import pickle
import requests
import pandas as pd
from firebase_admin import firestore


db = firestore.client()
st.session_state.db = db
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def get_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=916fe9b507a008af1dcef134a2177b06'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def search_recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    measured_distance = similarity[index]
    list_movies = sorted(list(enumerate(measured_distance)), reverse=True,key=lambda x:x[1])[1:7]

    recommended_movies = []
    posters = []
    print(list_movies)
    for i in list_movies:
        print(i[0])
        movie_id = movies.iloc[i[0]].movie_id
        print(movie_id, 32)
        recommended_movies.append(movies.iloc[i[0]].title)
        posters.append(get_poster(movie_id))
    return recommended_movies, posters


def app():
    
    st.title('Movie Recommendation System')

    option = st.selectbox(
        'Enter Movies',
        movies['title'].values
    )

    if st.button('Recommend'):

        if 'username' in st.session_state and st.session_state["signedout"] == True:
            col1, col2, col3, col4, col5, col6 = st.columns(6)
            
            recommendations, posters = search_recommend(option)

            with col1:
               st.text(recommendations[0])
               st.image(posters[0])
            with col2:
                st.text(recommendations[1])
                st.image(posters[1])
            with col3:
               st.text(recommendations[2])
               st.image(posters[2])
            with col4:
                st.text(recommendations[3])
                st.image(posters[3])
            with col5:
               st.text(recommendations[4])
               st.image(posters[4])
            with col6:
                st.text(recommendations[5])
                st.image(posters[5])
            
            info = db.collection('History').document(st.session_state.username).get()

            if info.exists:
                info = info.to_dict()
                if 'Content' in info.keys():
                    new = db.collection('History').document(st.session_state.username)
                    new.update({u'Content': firestore.ArrayUnion([u'{}'.format(option)])})
            else:
                data = {"Content":[option], "Username":st.session_state.username}
                db.collection('History').document(st.session_state.username).set(data)  
        else:
            st.warning('Please Login/SignUp')