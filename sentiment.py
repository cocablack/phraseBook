import getopt				# args
import logging				# logging    
import sqlite3

from textblob import TextBlob
    
database_path = "sentiment.db"
    
conn = None
cur = None
    
def query(json_data):
    """ TODO
    Queries for book recommendations based off of the json_data we receive from
    the user
    
    """
    global conn
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM Texts WHERE Sentiment=0.5")
    rows = cur.fetchall()
    
    for row in rows:
        print(row)
    
    result = {}
    result["data"] = "hello world"
    
    return result
    
def load_database():
    global conn
    if not conn:
        conn = sqlite3.connect(database_path)

def create_database():
    texts = []
    
    def parse_text(url):
    
        return (a,b,c,d)
    
    texts.append((5, "title_1", "author_1", 0.5))
    texts.append((6, "title_2", "author_2", 0.6))
    texts.append((7, "title_3", "author_3", 0.7))
    texts.append((8, "title_4", "author_4", 0.54))
    texts.append((9, "title_5", "author_5", 0.22))
    texts.append((10, "title_6", "author_6", 0.32))
    

    # Save our results to the database    
    
    global conn
    
    conn = sqlite3.connect(':memory:')
    with conn:
        cur = conn.cursor()
            
        cur.execute("DROP TABLE IF EXISTS Texts")
        cur.execute("CREATE TABLE Texts(Id INT, Title TEXT, Author TEXT, Sentiment REAL)")        
        cur.executemany("INSERT INTO Texts VALUES(?, ?, ?, ?)", texts)
        
        data = '\n'.join(conn.iterdump())
        
        logging.info("Writing to Database %s", database_path)
        with open(database_path, 'w') as f:
            f.write(data)
        
if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:\t%(message)s', level=logging.DEBUG)
    create_database()
    
    load_database()
    query(None)
    logging.info("Exiting")