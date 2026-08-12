def count_words(sentence):
    sentence=sentence.lower()
    words=sentence.split()
    word_frequency={}
    for word in words:
        if word in word_frequency:
            word_frequency[word]+=1
        else:
           word_frequency[word]=1
    return word_frequency
sentence=input("Enter a sentence:")
result=count_words(sentence)
print("Word Frequencies:",result)
print("Total number of words:",len(sentence.split()))
print("Number of unique words:",len(result))