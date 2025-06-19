from transformers import pipeline
from sklearn_som.som import SOM
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from .models import WordInput
import numpy as np
import random
import pickle


def index(request):
    return render(request, "word_retrieval/index.html")


def result(request, word="Hello"):
    # get word from form
    if request.GET:
        word = request.GET
        word = word.dict()
        word = word['word_input']
    # initialize feature extraction object using pipeline
    feature_extractor = pipeline("feature-extraction", framework="pt", model="facebook/bart-base")
    # create word list to feed to feature extractor
    words = ["Hello", word]
    # create list of vector embeddings for words
    embeddings = [feature_extractor(words[0], return_tensors="pt")[0].numpy().mean(axis=0),
                  feature_extractor(words[1], return_tensors="pt")[0].numpy().mean(axis=0)]
    # make numpy array
    embeddings = np.array(embeddings)
    # open the saved ML model
    with open('../word_som.pkl', 'rb') as file:
        word_som = pickle.load(file)
    # retrieve word prediction as word id
    word_id = word_som.predict(embeddings)
    # retrieve only the id of word submitted
    word_id = word_id[1]
    # retrieve the word from the database
    w = get_object_or_404(WordInput, user_text__exact=str(word_id+1))
    # retrieve all similar words
    words = list(w.wordoutput_set.all())
    # choose up to 5 random words from the associated words list
    word_sample = random.sample(words, min(5, len(words)))
    context = {"word": word,
               "word_id": word_id,
               "word_sample": word_sample}
    return render(request, "word_retrieval/result.html", context)
