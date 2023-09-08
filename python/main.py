import sys

from database import Database
from uploader import Uploader
from embeddings import Embeddings

if __name__ == '__main__':
    
    embeddings = Embeddings()
    try:
        instruction = sys.argv[1].lower()
        data = sys.argv[2].lower()
    except IndexError:
        print('No instructions or data given. Please type -u, -p, -e, -d')
        exit()
    
    if (instruction == '-u'):
        Uploader(data)
    
    else:
        vector = embeddings.get_embedding(data)
        if (instruction == '-p'):
            db = Database(name = 'podcast')
            print(db.query(vector, index = 'podcast'))

        elif (instruction == '-e'):
            db = Database(name = 'episode')
            print(db.query(vector, index = 'episode'))

        elif (instruction == '-d'):
            db = Database(name = 'description')
            print(db.query(vector, index = 'description'))
