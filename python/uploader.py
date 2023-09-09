import os
import pandas as pd
from tqdm import tqdm

from constants import *
from database import Database
from embeddings import Embeddings

class Uploader:
    def __init__(self, data):
        self.upload_embeddings(data)

    def upload_embeddings(self, data):
        embeddings = Embeddings()
        db = Database(name = data.split('.')[0])
        df = pd.read_csv(os.path.join(PATH_DATA, data))
        
        for index, row in tqdm(df.iterrows(), total = df.shape[0]):
            if (len(row['title']) > 0):
                vector = embeddings.get_embedding(row['title'])
                db.write(row['title'], vector, index = data.split('.')[0])
