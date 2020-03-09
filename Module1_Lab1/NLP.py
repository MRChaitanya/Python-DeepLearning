from bs4 import BeautifulSoup
import requests

file = open("nlp_input.txt", "r")
string = file.read()
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')

stokens = nltk.sent_tokenize(string)
wtokens = nltk.word_tokenize(string)

tagged = nltk.pos_tag(wtokens)
for k in tagged:
    print(k)

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
for t in wtokens[:100]:
    print("Lemmatizer:", lemmatizer.lemmatize(t), ",    With POS=n:", lemmatizer.lemmatize(t, pos="n"))

from nltk.util import ngrams

token = nltk.word_tokenize(string)

for s in stokens[:50]:
    trigrams = list(ngrams(token, 3))
    print("The text:", s, "\ntrigrams", trigrams)

from nltk import word_tokenize, pos_tag, ne_chunk

for s in stokens[:50]:
    print(ne_chunk(pos_tag(word_tokenize(s))))
Lstemmer = nltk.LancasterStemmer()
