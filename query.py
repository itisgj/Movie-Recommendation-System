import streamlit as st
import pickle
import requests
import pandas as pd
from firebase_admin import firestore
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel



db = firestore.client()
st.session_state.db = db
movies_list = pickle.load(open('movies.pkl', 'rb'))
movies = pd.DataFrame(movies_list)



def get_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=916fe9b507a008af1dcef134a2177b06'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

def query_recommend(actor_1, actor_2, director, genre, desc):
    
    actor_1_combined  = actor_1.replace(" ","")
    actor_2_combined  = actor_2.replace(" ","")
    director_combined  = director.replace(" ","")
    genre_combined  = genre.replace(" ","")

    actor_1_combined.lower()
    actor_2_combined.lower()
    director_combined.lower()
    genre_combined.lower()
    desc_combined = desc.lower()


    combined_feature = movies['cast'] + ' ' + movies['crew'] + ' ' + movies['genres'] + ' ' + movies['desc']

    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf_vectorizer.fit_transform(combined_feature)

    user_queries = [actor_1_combined.lower(), actor_2_combined.lower(), director_combined.lower(), genre_combined.lower(), desc_combined.lower()]
    user_queries_vector = tfidf_vectorizer.transform(user_queries)

    similarities = linear_kernel(user_queries_vector, tfidf_matrix)

    avg_similarity = similarities.mean(axis=0)
    movie_indices = avg_similarity.argsort()[::-1][:10]
  
    top_recommendations = movies.iloc[movie_indices].movie_id
    query_res = list(top_recommendations)

    recommennded_movies = []
    posters = []

    for i in query_res:
        recommennded_movies.append(movies.set_index('movie_id').loc[i, 'title'])
        posters.append(get_poster(i))

    return recommennded_movies, posters
    

def app():
    row_input = st.columns((1,1,1))
    with row_input[0]:
        actor_1 = st.text_input("Actor 1",key="Actor 1",max_chars=20)
    with row_input[1]:
         actor_2 = st.text_input("Actor 2",key="Actor 2",max_chars=20)
    with row_input[2]:
         director = st.text_input("Director",key="Director",max_chars=20)
    genre = st.text_input("Genre",key="Genre",max_chars=20)
    desc = st.text_area("Description",max_chars=50)


    if st.button('Recommed'):
        
        if 'username' in st.session_state and st.session_state["signedout"] == True:
            col1, col2, col3, col4, col5, col6, col7, col8, col9, col0 = st.columns(10)

            recommendations, posters = query_recommend(actor_1, actor_2, director, genre, desc)

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

            with col7:
               st.text(recommendations[6])
               st.image(posters[6])
            with col8:
               st.text(recommendations[7])
               st.image(posters[7])
            with col9:
               st.text(recommendations[8])
               st.image(posters[8])
            with col0:
               st.text(recommendations[9])
               st.image(posters[9])
        else:
            st.warning('Please Login/SignUp')