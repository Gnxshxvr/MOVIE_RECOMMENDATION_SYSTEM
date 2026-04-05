#RAW PYTHON CODE

# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import difflib #to make sure even if user gives value wrong it will find nearby value
from sklearn.feature_extraction.text import TfidfVectorizer #textual data to meaning numbers -> vectors
from sklearn.metrics.pairwise import cosine_similarity #similarilty confidence score using cosine similarity btwn 0<x<1

# DATA COLLECTION AND PREPROCESSING
movies_data = pd.read_csv('movies.csv') #reads csv file

# relevant features selection
selected_features = ['genres','keywords','tagline','cast','director']

# replace the null values with null string
for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')
# first genre - na - not available -> fill with ''next keyqword and .....

# combining all features selected
combined_features = movies_data['genres']+' '+movies_data['keywords']+' '+ movies_data['tagline']+' '+movies_data['cast']+' '+movies_data['director']

# converting text to featured vectors(numerical vectors) -> that is easy for cosine similarity
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features) #conversion

# CONSINE SIMILARITY
# getting the similarity score cosine simialrity
similarity = cosine_similarity(feature_vectors)

# creating a list with all the movie names given in the dataset
list_of_all_titles = movies_data['title'].tolist() #take to an list

# getting the movie name from user
movie_name = input("movie name")

# close match for the movie name entered ->
find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles) #difflab matches entered with the list and gives closest match or the same match

# find one closest match
close_match = find_close_match[0]

# finding the index of the movie with title
index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
# --> this will find index of the movie in dataset

# list of similar movies -->
similarity_score = list(enumerate(similarity[index_of_the_movie]))
# 1st index , 2 - similarity score with respected to entered movie ,

# soerting out the top
sorted_similar_movies = sorted(similarity_score, key = lambda x:x[1],reverse=True)
# x-> similarity_score , x[1] - 2nd element here 0.39348439 smtg , if x[0] -> index 0,1,2, Reverses it since reverse()

# print top similar similar movies based on index
print('movies suggested for you \n')
i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = movies_data[movies_data.index==index]['title'].values[0]
  if( i < 10):
    print(i, '.',title_from_index)
    i+=1
