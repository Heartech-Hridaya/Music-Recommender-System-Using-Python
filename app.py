import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
CLIENT_ID = "b056c1ead21c44c78cca68090f7b6164"
CLIENT_SECRET = "dd17f781bbfd4abfaa8f2730f4c87f10"

# Initialize Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to get album cover
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")
    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        return track["album"]["images"][0]["url"]
    else:
        return "https://i.postimg.cc/00NxYz4V/social.png"  # Fallback image

# Function to recommend songs
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)
    return recommended_music_names, recommended_music_posters

# Load data
music = pickle.load(open('df.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

# Set page config
st.set_page_config(page_title="🎵 Music Recommender", page_icon="🎧", layout="wide")

# Header Section
st.markdown("""
    <div style="text-align: center; margin-bottom: 2rem;">
        <h1 style="font-size: 3rem;">🎧 Music Recommender</h1>
        <p style="font-size: 1.2rem; color: #555;">Discover similar songs based on your favorite tracks!</p>
    </div>
""", unsafe_allow_html=True)

# Dropdown to select a song
movie_list = music['song'].values
selected_movie = st.selectbox(
    "🎶 Select a song you like:",
    movie_list,
    index=0
)

# Recommendation button
if st.button('🔍 Show Recommendations'):
    recommended_music_names, recommended_music_posters = recommend(selected_movie)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>🎼 Recommended Songs</h3>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    # Display results in a styled grid
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(recommended_music_posters[i], use_column_width=True)
            st.markdown(f"<div style='text-align: center; font-weight: bold; font-size: 16px;'>{recommended_music_names[i]}</div>", unsafe_allow_html=True)

    st.markdown("<br><hr>", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align: center; font-size: 0.9rem; color: #888;">
        Made with ❤️ using Streamlit and Spotify API By- <b>Hridaya Manandhar </b>
    </div>
""", unsafe_allow_html=True)
