# Taylor Swift Song Recommendation System

This project is a simple song recommendation system based on lyrics similarity. It utilizes **Cosine Similarity** to recommend songs similar to a given song based on their lyrics.

## How It Works

The recommendation system follows these steps:

### 1. **Check if the Song Exists**
- The system checks if the given song title exists in the dataset. If the song title is not found, it returns an empty list.

### 2. **Find the Song Index**
- The system identifies the index of the song in the dataset using the song title (`songs['song_title'] == song_title`), which determines where in the lyrics matrix to look.

### 3. **Calculate Cosine Similarity**
- **Cosine Similarity** is used to measure the similarity between two songs' lyrics by treating the lyrics as vectors in a multi-dimensional space. The cosine similarity value ranges from `-1` to `1`, where `1` means the lyrics are identical, and `0` means they are completely dissimilar.
- The system calculates the cosine similarity between the given song's lyrics and all other songs' lyrics in the dataset.

### 4. **Get Similar Songs**
- The songs are sorted based on their similarity scores in descending order, excluding the input song itself. The top `num_recommendations` most similar songs are selected.

### 5. **Return Recommendations**
- The system returns the titles and artist names of the most similar songs as a list of dictionaries, formatted as a JSON response.

## Features
-  Recommends similar songs based on lyrics
-  Uses TF-IDF and Cosine Similarity for NLP-based song matching
-  Simple web interface with Flask backend
-  Lightweight and easy to set up



## Tech Stack
- **Backend:** Flask (Python)
- **NLP & Data Processing:** Pandas, Scikit-learn (TF-IDF, Cosine Similarity)
- **Frontend:** HTML, CSS, JavaScript (Fetch API)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/ffrhnaa7/song-recommender.git
   cd song-recommender
   ```

2. Install dependencies:
   ```bash
   pip install flask pandas scikit-learn
   ```

3. Run the Flask server:
   ```bash
   python app.py
   ```

4. Open `index.html` in your browser or visit `http://127.0.0.1:5000`.

## Usage
1. Enter a song title in the search bar.
2. Click "Recommend" to get similar song suggestions.
3. Enjoy discovering new music!

## Dataset
- Uses a CSV file with columns: `song_title`, `artist`, `lyrics`.
- You can replace `songs.csv` with your own dataset.

---
Made with ❤️ for music lovers! 🎧

