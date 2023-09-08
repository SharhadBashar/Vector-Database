import os

PATH_CONFIG = '../config/'
PATH_DATA = '../data/'
PATH_DUMP = os.path.join(PATH_DATA, 'dump/')
PATH_DUMP_TXT = os.path.join(PATH_DUMP, 'error.txt')
PATH_CONFIG_PINECONE = os.path.join(PATH_CONFIG, 'pinecone.json')
PATH_DATA_CSV = os.path.join(PATH_DATA, 'data.csv')

INDEX = ['all', 'description', 'episode', 'podcast']

MODELS = {
    'mpnet_base_v2': {
        'name': 'sentence-transformers/all-mpnet-base-v2',
        'shape': 768
    },
    'minilm_v2': {
        'name': 'sentence-transformers/all-MiniLM-L6-v2',
        'shape': 384
    }
}