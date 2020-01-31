infile=open("sample.txt","r")
wordcount={}
for word in infile.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
print (word,wordcount)
infile.close();