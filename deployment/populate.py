import os
import django
import numpy as np
import pandas as pd
from django.utils import timezone

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'word_suggestions.settings')
django.setup()

from word_retrieval.models import WordInput

# import list of most common English words
words = pd.read_csv("../common_words.csv")
# import list of word predictions
word_categories = pd.read_csv("../word_categories.csv")

# convert into a suitable format
words = np.array(words['word'])
word_categories = np.array(word_categories['80'])
# fix length mismatch
words = np.delete(words, -1)

for i in range(100):
    w = WordInput(user_text=str(i+1), req_date=timezone.now())
    w.save()
    for j in words[word_categories == i]:
        w.wordoutput_set.create(return_text=j)

print("Database populated successfully.")
