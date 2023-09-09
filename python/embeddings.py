from sentence_transformers import SentenceTransformer

from constants import *

class Embeddings:
    def __init__(self, model = 'mpnet_base_v2'):
        self.model = SentenceTransformer(MODELS[model]['name'])

    def get_embedding_shape(self, embedding):
        return embedding.shape

    def get_embedding(self, sentence):
        try:
            return self.model.encode(sentence).tolist()
        except Exception as e:
            with open(PATH_DUMP_TXT, 'a') as error_file:
                error_file.write('EMBEDDINGS ::: ', + sentence + ' ERROR ::: ' + e + '\n')

    def get_embeddings(self, sentences):
        return self.model.encode(sentences).tolist()
