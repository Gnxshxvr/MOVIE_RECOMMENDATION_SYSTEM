# 🎬 MOVIE_RECOMMENDATION_SYSTEM

A **Content-Based Movie Recommendation System** built using Python and Google Colab that suggests similar movies based on genres, keywords, cast, tagline, and director.

---

## 🚀 Live Project

👉 GitHub Repo: https://github.com/Gnxshxvr/MOVIE_RECOMMENDATION_SYSTEM

---

## 📌 Overview

This project recommends movies by analyzing their content features and finding similarities using **TF-IDF vectorization** and **cosine similarity**.

Even if the user enters a **wrong or slightly misspelled movie name**, the system intelligently finds the closest match using Python’s `difflib`.

---

## 🧠 Core Idea

The system works by:

* Combining important features:

  * Genres 🎭
  * Keywords 🔑
  * Tagline 📝
  * Cast 👨‍🎤
  * Director 🎬

* Converting text → numerical vectors using **TF-IDF**

* Calculating similarity between movies using **cosine similarity**

* Recommending top similar movies

---

## ⚙️ Workflow

```mermaid
flowchart LR
A[User inputs movie] --> B[Find closest match using difflib]
B --> C[Extract combined features]
C --> D[Convert to TF-IDF vectors]
D --> E[Compute cosine similarity]
E --> F[Sort similar movies]
F --> G[Display top recommendations]
```

---

## 🛠️ Tech Stack

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* Difflib
* Google Colab

---

## 📂 Dataset

* movies.csv
* Contains:

  * Title
  * Genres
  * Keywords
  * Tagline
  * Cast
  * Director

---

## ▶️ How to Run

### 🔹 Google Colab

1. Upload `movies.csv`
2. Open the notebook
3. Run all cells
4. Enter a movie name when prompted

---

### 🔹 Local Setup

```bash
git clone https://github.com/Gnxshxvr/MOVIE_RECOMMENDATION_SYSTEM.git
cd MOVIE_RECOMMENDATION_SYSTEM
pip install pandas numpy scikit-learn
python movie_recommendation_system.py
```

---

## 💻 Key Code Logic

From your implementation:

```python
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)

similarity = cosine_similarity(feature_vectors)
```

👉 This converts text → vectors and computes similarity scores.

---

### 🔍 Smart Movie Matching

```python
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
```

👉 Handles typos and incorrect inputs.

---

## 🧪 Example

Input:

> avatr

Output:

* Avatar
* Guardians of the Galaxy
* John Carter
* Avengers
* Star Trek

---

## ✨ Features

* 🔍 Accepts user input
* 🤖 Handles spelling mistakes
* 🎯 Accurate recommendations
* ⚡ Fast execution
* 🧠 ML-based approach

---

## 🔮 Future Improvements

* 🎨 Add Streamlit UI
* 🎥 Show movie posters (TMDB API)
* 🌐 Deploy as a web app
* 🤝 Add collaborative filtering

---

GitHub: https://github.com/Gnxshxvr

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

---
