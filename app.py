import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ce2a128e9a68a49f58d0a394a1b7efd7&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def fetch_rating(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ce2a128e9a68a49f58d0a394a1b7efd7&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    rating = data['vote_average']
    return round(rating)

def fetch_tagline(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=ce2a128e9a68a49f58d0a394a1b7efd7&language=en-US".format(
        movie_id)
    data = requests.get(url)
    data = data.json()
    tag = data['tagline']
    return tag
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:16]
    recommended_movies = []
    recommended_movies_posters = []
    recommended_movies_rating = []
    recommended_movies_tag = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))
        recommended_movies_rating.append(fetch_rating(movie_id))
        recommended_movies_tag.append(fetch_tagline(movie_id))
    return recommended_movies, recommended_movies_posters, recommended_movies_rating, recommended_movies_tag


movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.markdown("[![in](linkedin.png)](http://www.linkedin.com/in/ashutosh-tripathy-9b05aa203)")
st.title('Movies for You')

movie_list = movies['title'].values
selected_movie_name = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Recommend'):
    recommended_movies, recommended_movies_posters, recommended_movies_rating, recommended_movies_tag = recommend(selected_movie_name)

    col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)
    with col1:
        st.text(recommended_movies[0])
        st.image(recommended_movies_posters[0])
        st.text(recommended_movies_rating[0])
        st.markdown(recommended_movies_tag[0])
    with col2:
        st.text(recommended_movies[1])
        st.image(recommended_movies_posters[1])
        st.text(recommended_movies_rating[1])
        st.markdown(recommended_movies_tag[1])
    with col3:
        st.text(recommended_movies[2])
        st.image(recommended_movies_posters[2])
        st.text(recommended_movies_rating[2])
        st.markdown(recommended_movies_tag[2])
    with col4:
        st.text(recommended_movies[3])
        st.image(recommended_movies_posters[3])
        st.text(recommended_movies_rating[3])
        st.markdown(recommended_movies_tag[3])
    with col5:
        st.text(recommended_movies[4])
        st.image(recommended_movies_posters[4])
        st.text(recommended_movies_rating[4])
        st.markdown(recommended_movies_tag[4])
    with col6:
        st.text(recommended_movies[5])
        st.image(recommended_movies_posters[5])
        st.text(recommended_movies_rating[5])
        st.markdown(recommended_movies_tag[5])
    with col7:
        st.text(recommended_movies[7])
        st.image(recommended_movies_posters[7])
        st.text(recommended_movies_rating[7])
        st.markdown(recommended_movies_tag[7])
    with col8:
        st.text(recommended_movies[8])
        st.image(recommended_movies_posters[8])
        st.text(recommended_movies_rating[8])
        st.markdown(recommended_movies_tag[8])
    with col9:
        st.text(recommended_movies[9])
        st.image(recommended_movies_posters[9])
        st.text(recommended_movies_rating[9])
        st.markdown(recommended_movies_tag[9])

st.markdown("[![Details]()](https://movies4u.s3.ap-south-1.amazonaws.com/mrs/mrs/index.html)")