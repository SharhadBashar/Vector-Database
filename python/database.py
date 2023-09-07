import json
import pinecone

from constants import *

class Database:
    def __init__(self, name = 'podcast'):
        with open(PATH_CONFIG_PINECONE) as config_file:
            config = config_file.read()
        config = json.loads(config)[name]
        pinecone.init(api_key = config['key'], environment = config['environment'])
        self.index = pinecone.Index(name)
        print(self.index)

    def get_indexes(self):
        print(self.cone.list_indexes())

    def get_index_info(self, index = 'all'):
        if (index not in INDEX):
            return ('Wrong index. Please pick one from {}'.format(INDEX))
        print(self.index.describe_index_stats())

    def create_index(self, index_name):
        self.pinecone.Index(index_name)

    def read(self, index = 'all'):
        None

    def write(self, key, value, index = 'all', model = 'mpnet_base_v2'):
        if (index not in INDEX):
            print('Wrong index. Please pick one from {}'.format(INDEX))
            return
        # if (len(value) != MODELS[model]['shape']):
        #     print('Length of value should be {}'.format(MODELS[model]['shape']))
        #     return
        self.index.upsert([
            (key, list(value))
        ])
        input()

    def query(self, value, index = 'all', model = 'mpnet_base_v2', k = 5):
        if (index not in INDEX):
            return ('Wrong index. Please pick one from {}'.format(INDEX))
        if (value.shape != MODELS[model]['shape']):
            return ('Length of value should be {}'.format(MODELS[model]['shape']))
        return self.index.query(
            vector = value,
            top_k = k,
            include_values = True
        )

    def delete_index(self, index_name):
        self.pinecone.delete_index(index_name)
