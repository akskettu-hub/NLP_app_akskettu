#An outline of the actual application for this project
from sklearn.feature_extraction.text import CountVectorizer

def main():
    pass


documents = ["This is a silly example",
            "A better example",
            "Nothing to see here",
            "This is a great and long example"]

cv = CountVectorizer(lowercase=True, binary=True)
sparse_matrix = cv.fit_transform(documents)

dense_matrix = sparse_matrix.todense()


td_matrix = dense_matrix.T   # .T transposes the matrix


terms = cv.get_feature_names_out()


t2i = cv.vocabulary_
    
    
d = {"and": "&", "AND": "&",
    "or": "|", "OR": "|",
    "not": "1 -", "NOT": "1 -",
    "(": "(", ")": ")"}          # operator replacements

def rewrite_token(t):
    return d.get(t, 'td_matrix[t2i["{:s}"]]'.format(t)) # Can you figure out what happens here?

def rewrite_query(query): # rewrite every token in the query
    return " ".join(rewrite_token(t) for t in query.split())

def test_query(query):
    print("Query: '" + query + "'")
    print("Rewritten:", rewrite_query(query))
    print("Matching:", eval(rewrite_query(query))) # Eval runs the string as a Python command
    print()
    
#test_query("example AND NOT beans")

def input_query():
    while True:
        print("Please input query:")
        user_input = input()
        if user_input == "quit" or user_input == "":
            break
        return user_input
    
def retrieve_matches(query):
    hits_matrix = eval(rewrite_query(query))
    hits_list = list(hits_matrix.nonzero()[1])
    return hits_list
        
def print_retrieved(hits_list):
    print(f"Found {len(hits_list)} matches:")
    
    print_limit = 2
    
    if len(hits_list) > print_limit:
        print(f"Here are the first {print_limit} results:")
        
        e_list = list(enumerate(hits_list))
        for i in range(print_limit):
            print("Matching doc #{:d}: {:s}".format(e_list[i][0], documents[e_list[i][1]]))
                
    else:        
        for i, doc_idx in enumerate(hits_list):
            print("Matching doc #{:d}: {:s}".format(i, documents[doc_idx]))
    
#test_query(input_query())

#print(retrieve_matches(input_query()))
print_retrieved(retrieve_matches(input_query()))