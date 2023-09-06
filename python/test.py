from sentence_transformers import SentenceTransformer, util
sentences = ['That is a happy person']
compare = ['That is a happy dog', 'That is a very happy person', 'Today is a sunny day']

model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')
embeddings = model.encode(sentences)
compare_embeddings = model.encode(compare)
print(embeddings.shape)
# for compare_embedding in compare_embeddings:
#     print(util.pytorch_cos_sim(embeddings, compare_embedding))
