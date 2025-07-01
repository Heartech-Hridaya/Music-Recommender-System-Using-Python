 🎧 Music Recommender System

An interactive web app that recommends similar songs based on your favorite track — built using **Streamlit**, **Machine Learning**, and the **Spotify API**.

🚀 Features

- 🔍 Recommends songs based on lyrical similarity using TF-IDF and cosine similarity
- 🎨 Clean, interactive UI built with Streamlit
- 🎵 Pulls real-time album cover images using the Spotify Web API
- 🧠 Uses NLP preprocessing to understand lyrical context
- ⚡ Lightweight and fast - works on local machines or deploys easily to the web



 🧠 How It Works

1. Data Preprocessing: Song lyrics are cleaned, tokenized, and stemmed.
2. Vectorization: Lyrics are transformed using `TfidfVectorizer`.
3. Similarity Matching: Cosine similarity is computed between all songs.
4. Recommendation: Given a song, the top 5 lyrically similar songs are displayed.
5. Spotify Integration: Album art is fetched via Spotipy (Spotify Web API wrapper).

---

 📦 Tech Stack

- Frontend: Streamlit
- ML/NLP: Pandas, NLTK, Scikit-learn
- API: Spotipy (Spotify Web API)
- Language: Python
