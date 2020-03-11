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
for t in wtokens[:10]:
    print("Lemmatizer:", lemmatizer.lemmatize(t), ",    With POS=n:", lemmatizer.lemmatize(t, pos="n"))

from nltk.util import ngrams

token = nltk.word_tokenize(string)

for s in stokens[:10]:
    trigrams = list(ngrams(token, 3))
    print("The text:", s, "\ntrigrams", trigrams)

wordfreq = nltk.FreqDist(trigrams)
mostcommon = wordfreq.most_common(10)
print("Most frequently repeated top 10 trigrams:", mostcommon)

sentTokens = nltk.sent_tokenize(string)
concatenatedArray = []
for sentence in sentTokens:
    for (i, j, k) in trigrams:
        for ((l, m, n), length) in mostcommon:
            if (i,j,k == l, m, n):
                concatenatedArray.append(sentence)

print("\nConcatenated sentenced is:", concatenatedArray)
