import streamlit as st
import spotipy
import webbrowser
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
SPOTIFY_CLIENT_ID = "1746781a5bf14399be9b5b9528427e5d"
SPOTIFY_CLIENT_SECRET = "862ddf3c74fe4f628dfbf2ccea02265a"

# Authenticate with Spotify
auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Streamlit UI
st.title("Emotion-Based Music Recommender 🎧")

emotion = st.selectbox("Choose your emotion", ["Happy", "Sad", "Angry", "Relaxed"])

if st.button("Recommend Songs"):
    st.subheader(f"Top Spotify Songs for: {emotion}")

    # Search query based on emotion
    results = sp.search(q=emotion + " mood", type='track', limit=5)
    tracks = results['tracks']['items']

    if tracks:
        # Open the first track in browser
        first_track_url = tracks[0]['external_urls']['spotify']
        webbrowser.open_new_tab(first_track_url)  # Auto-open in browser

        # List all tracks
        for idx, track in enumerate(tracks):
            name = track['name']
            artist = track['artists'][0]['name']
            url = track['external_urls']['spotify']
            st.write(f"{idx+1}. [{name} - {artist}]({url})")
    else:
        st.warning("No songs found. Try a different emotion.")
