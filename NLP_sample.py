import nltk # Natural Language Tool Kit
"""
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('punkt_tab')
"""
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

sentence1 = "Earth is the third planet from the sun"

sentence2 = "Jupiter is the largest planet"

stopwords = set(stopwords.words('english'))

def nlp_preprocess(text):

    tokens = word_tokenize(text=text)

    new = [i for i in tokens if i not in stopwords]

    return " ".join(new)

s1 = nlp_preprocess(sentence1)
s2 = nlp_preprocess(sentence2)

print(s1)
print(s2)

tfid = TfidfVectorizer()

result_matrix = tfid.fit_transform([s1,s2])

print(result_matrix)

simi = cosine_similarity(result_matrix[0],result_matrix[1])

print(f"The similarity in between s1 and s2 is {simi}")