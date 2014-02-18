train_set = ("The sky is blue.", "The sun is bright.")
test_set = ("The sun in the sky is bright.",
"We can see the shining sun, the bright sun.")
from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()

print vectorizer
CountVectorizer(analyzer__min_n=1,
analyzer__stop_words=set(['all', 'six', 'less', 'being', 'indeed']) 
vectorizer.fit_transform(train_set)
print vectorizer.vocabulary
{'blue': 0, 'sun': 1, 'bright': 2, 'sky': 3}
