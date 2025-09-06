import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    print(f"Movies Similar to {movie} are :\n")
    recommended_movies=[]
    for i in movies_list:
        movie_id=i[0]
        #fetch poster from api
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


similarity = pickle.load(open('similarity.pkl','rb'))

movies = pickle.load(open("movies.pkl",'rb'))
movies_list=movies['title'].values

st.title('Movie Recommender System')

selected_movie_name= st.selectbox(
    'Select movie name',
    movies_list
)

if st.button(f'Similar movies to {selected_movie_name}'):
    recommendations=recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)