import streamlit as st
import pickle
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append((movies.iloc[i[0]].title))
    return recommended_movies



movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

st.title('Movie Recommender System')

st.write('Welcome to the Movie Recommender Application by Sanjay. Select the movie for which you would like similar movies for using the dropdown below: ')
selected_movie_name = st.selectbox(
    '',
    sorted(movies['title'].values)
)
st.write('')
if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)