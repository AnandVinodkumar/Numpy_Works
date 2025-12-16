# Natural Language Processing
# -------------------------------------------
"""
A field of AI that enables computers to understand,
interpret and generate human language

Converts our language into machine knowing language
"""

# Preprocessing steps (Optional)
#--------------------------------------------------
"""
1) Remove unwanted white spaces
2) Convert all characters into ASCII
3) Expand shortforms
4) Remove unwanted characters #%&*_-
"""

# Must be implemented steps
"""
django is a API mastering tool

stopwords (almost 180 stopwords)

Eg: Universities are amazing places for studying and learning new things
stopwords are 'are','and','is','the','those','that',..................180

Convert all characters to lowercase

lemmatization / stemming >>> Removes -ing (Tail part of the words) from words to find the root words

Tokenization
--------------------------------------
n-gram method >> takes n words from a sentence as a token

"vinay is a good boy" Splits using whitespaces
# vinay
# is
# a
# good
# boy
this is 1-gram method


# Vectorization

Term Frequency(text) = Total no. of [word] in text
                        -----------------------------
                        Total words in text

IDF (Inverse Document Frequency) = N / df(word)
        N -> No of sentences  df(word) -> total frequency of (word) in both sentences

"""