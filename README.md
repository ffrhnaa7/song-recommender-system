# 🎵 Basic Song Recommendation App

A simple song recommendation app that suggests similar songs based on lyrics similarity using NLP techniques.

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

