# Figuring out search engine stuff from week 2
from sklearn.feature_extraction.text import CountVectorizer

documents = ["This is a silly example",
             "A better example",
             "Nothing to see here",
             "This is a great and long example"]

cv = CountVectorizer(lowercase=True, binary=True)
sparse_matrix = cv.fit_transform(documents)

print("Term-document matrix: (?)\n")
print(sparse_matrix)