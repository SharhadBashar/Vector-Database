# from sentence_transformers import SentenceTransformer, util
# sentences = ['That is a happy person']
# compare = ['That is a happy dog', 'That is a very happy person', 'Today is a sunny day']

# model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
# embeddings = model.encode(sentences)
# compare_embeddings = model.encode(compare)
# print(embeddings.shape)
# # for compare_embedding in compare_embeddings:
# #     print(util.pytorch_cos_sim(embeddings, compare_embedding))






import numpy as np
import json
import pinecone

with open('../config/pinecone.json') as config_file:
    config = config_file.read()
config = json.loads(config)['podcast']

pinecone.init(api_key = config['key'], environment = config['environment'])

index = pinecone.Index('podcast')

# index.upsert([
#     ("A", decimal_array)
# ])

print(index.describe_index_stats())