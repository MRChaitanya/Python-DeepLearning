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

for s in stokens[:100]:
    trigrams = list(ngrams(token, 3))
    print("The text:", s, "\ntrigrams", trigrams)

wordfreq = nltk.FreqDist(trigrams)
mostcommon = wordfreq.most_common(10)
print("Most frequently repeated top 10 trigrams:", mostcommon)

sentTokens = nltk.sent_tokenize(string)
concatenatedArray = []
for sentence in sentTokens:
    for a,b,c in trigrams:
        for ((d,e,f),length) in mostcommon:
            if(a == d,e,f):
                concatenatedArray.append(sentence)
print("Concatenated sentenced is:", concatenatedArray)
print("Maximum of concatenated is ", max(concatenatedArray))


