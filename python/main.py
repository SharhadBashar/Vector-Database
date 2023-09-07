import os
import numpy as np
import pandas as pd
from tqdm import tqdm

from constants import *
from database import Database
from embeddings import Embeddings

class Runner:
    def __init__(self, data):
        # self.create_embeddings(data)
        self.upload_embeddings(data)
        
    def create_embeddings(self, data):
        embeddings = Embeddings()
        df = pd.read_csv(os.path.join(PATH_DATA, data))
        sentences = df['PodcastName'].tolist()
        vectors = embeddings.get_embeddings(sentences)
        df['embeddings'] = vectors.tolist()
        df.to_csv(os.path.join(PATH_DATA, data), index = False)

    def upload_embeddings(self, data):
        df = pd.read_csv(os.path.join(PATH_DATA, data))
        db = Database(name = 'podcast')
        for index, row in tqdm(df.iterrows(), total = df.shape[0]):
            db.write(row['PodcastName'], row['embeddings'], index = 'podcast')
            
Runner('podcast.csv') 