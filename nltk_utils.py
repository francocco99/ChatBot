import nltk
from nltk.stem.snowball import SnowballStemmer
#nltk.download('punkt') package with pre trained tokenizer
stemmer=SnowballStemmer("italian")

def tokenizer(sentence):
    return nltk.word_tokenize(sentence)
def stem(word):
    return stemmer.stem(word.lower())

def bag_of_words(tokenized_sentece, words):
    pass

