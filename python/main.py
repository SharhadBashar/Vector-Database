import numpy as np
import json
import pinecone


with open('../config/pinecone.json') as config_file:
    config = config_file.read()
config = json.loads(config)

pinecone.init(api_key = config['key'], environment = config['environment'])

index = pinecone.Index('podcast')
decimal_array = list(np.random.uniform(low=0, high=1, size=1024))

# index.upsert([
#     ("A", decimal_array)
# ])

print(index.describe_index_stats())
