print('Hello, world!')
# create an object for TfidfVectorizer: tfidf_vector
tfidf_vector = TfidfVectorizer(stop_words='english')

# apply the object to the genres column: tfidf_matrix
tfidf_matrix = tfidf_vector.fit_transform(movies['genres'])

# create the cosine similarity matrix: sim_matrix
sim_matrix = linear_kernel(tfidf_matrix, tfidf_matrix)
