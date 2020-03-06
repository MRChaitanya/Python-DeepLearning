from bs4 import BeautifulSoup
import requests

URL = 'https://en.wikipedia.org/wiki/Google'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser').prettify()

text = str(soup.encode("UTF-8"))
file = open("input.txt", "w")
file.write(text)
file.close()

import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')

for k in text.split("\n"):
    text1 = str(nltk.re.sub(r"[^a-zA-Z0-9]+", ' ', k))
    file = open("input1.txt", "w")
    file.write(text1)

stokens = nltk.sent_tokenize(text1)
wtokens = nltk.word_tokenize(text1)
for s in stokens:
    print(s)

tagged = nltk.pos_tag(wtokens)
for k in tagged:
    print(k)

from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer

pStemmer = PorterStemmer()
lStemmer = LancasterStemmer()
sStemmer = SnowballStemmer('english')

for w in wtokens[:50]:
    print(pStemmer.stem(w), lStemmer.stem(w), sStemmer.stem(w))

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
for t in wtokens[:50]:
    print("Lemmatizer:", lemmatizer.lemmatize(t), ",    With POS=n:", lemmatizer.lemmatize(t, pos="n"))

from nltk.util import ngrams

token = nltk.word_tokenize(text1)

for s in stokens[:50]:
    token = nltk.word_tokenize(s)
    bigrams = list(ngrams(token, 2))
    trigrams = list(ngrams(token, 3))
    print("The text:", s, "\nword_tokenize:", token, "\nbigrams:", bigrams, "\ntrigrams", trigrams)

from nltk import word_tokenize, pos_tag, ne_chunk

for s in stokens[:50]:
    print(ne_chunk(pos_tag(word_tokenize(s))))
Lstemmer = LancasterStemmer()

