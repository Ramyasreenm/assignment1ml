#Split methods and set to get the unique words.
sentence = "I am a teacher and I love to inspire and teach people"
sentence_words = sentence.split()
unique_words = set(sentence_words)
print("Number of unique words are",len(unique_words))
print("Unique words are:",unique_words)