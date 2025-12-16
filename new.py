from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

s1 = "Jupiter is the fifth planet from the sun"

s2 = "Jupiter is the largest planet"

sentences = [s1,s2]

tfid = TfidfVectorizer()

result = tfid.fit_transform(sentences) # result will be a matrix

similarity = cosine_similarity(result[0],result[1])

print(similarity)