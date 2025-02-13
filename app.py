from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load dataset
songs = pd.read_csv("songs.csv")

# Preprocess and compute TF-IDF matrix
vectorizer = TfidfVectorizer(stop_words='english')
lyrics_matrix = vectorizer.fit_transform(songs['lyrics'].fillna(''))

def get_recommendations(song_title, num_recommendations=5):
    if song_title not in songs['song_title'].values:
        return []
    
    idx = songs[songs['song_title'] == song_title].index[0]
    similarities = cosine_similarity(lyrics_matrix[idx], lyrics_matrix).flatten()
    similar_indices = similarities.argsort()[-(num_recommendations+1):-1][::-1]
    
    return songs.iloc[similar_indices][['song_title', 'album']].to_dict(orient='records')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['GET'])
def recommend():
    song_title = request.args.get('song', '')
    recommendations = get_recommendations(song_title)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)

