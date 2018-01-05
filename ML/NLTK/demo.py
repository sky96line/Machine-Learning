from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

nltk.download('punkt')
stmt = "Hello there, my name is akash buch and i am the one who awsome."

words = word_tokenize(stmt)

print(words)