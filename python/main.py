import sys
from pprint import pprint

from helper import *
from database import Database
from uploader import Uploader
from embeddings import Embeddings

if __name__ == '__main__':
    
    embeddings = Embeddings()
    try:
        instruction = sys.argv[1].lower()
        data = sys.argv[2].lower()
    except IndexError:
        print('No instructions or data given. Please type -u, -p, -e, -d, -a')
        exit()
    
    if (instruction == '-u'):
        Uploader(data)
    
    else:
        vector = embeddings.get_embedding(data)
        if (instruction == '-p'):
            db = Database(name = 'podcast')
            pprint(print_query(db.query(vector, index = 'podcast'), data))

        elif (instruction == '-e'):
            db = Database(name = 'episode')
            pprint(print_query(db.query(vector, index = 'episode'), data))

        elif (instruction == '-d'):
            db = Database(name = 'description')
            pprint(print_query(db.query(vector, index = 'description'), data))

        elif (instruction == '-a'):
            db = Database(name = 'all')
            pprint(print_query(db.query(vector, index = 'all'), data))