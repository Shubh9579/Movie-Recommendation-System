import streamlit as st
import pickle
import pandas as pd 

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movie_list = sorted(list(enumerate(similarity[movie_index])),reverse=True,key = lambda x: x[1])
    
    recommended_movies=[]
    for i in movie_list[1:6]:
        movie_id = i[0]
        # fetch poster
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movie_dict = pickle.load(open('movies_dict.pkl','rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'How could you like to Contact',
    movies['title'].values)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
      st.write(i)