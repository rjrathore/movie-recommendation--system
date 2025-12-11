import streamlit as st
import pickle
import pandas as pd

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))     # full dataframe
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movie = []
    for i in movie_list:
        recommended_movie.append(movies.iloc[i[0]].title)
    return recommended_movie

st.title('Movie Recommendation System')

movie_list = movies['title'].values

selected_movie_name = st.selectbox(
    'Select a movie to get recommendations:',
    movie_list
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
