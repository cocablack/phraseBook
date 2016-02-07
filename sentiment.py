import getopt				# args
import logging				# logging    
import sqlite3
import os

from textblob import TextBlob
from media_analysis import analysis
    
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

def create_database(media_type):
    texts = []
    result = analysis(media_type)
    
    def parse_text(url):
    
        return (a,b,c,d,e,f,g)

    for k,v in result.items():
        l = result[k]
        for i in range(7):
            texts.append(l[i])

    
    # Save our results to the database    
    
    global conn
    
    conn = sqlite3.connect(':memory:')
    with conn:
        cur = conn.cursor()
            
        cur.execute("DROP TABLE IF EXISTS Texts")
        cur.execute("CREATE TABLE Texts(Media TEXT, \
            Id INT, Title TEXT, Author TEXT, Link TEXT, \
            Sentiment INT, Common TEXT)")        
        cur.executemany("INSERT INTO Texts VALUES(?, ?, ?, ?, ?, ?, ?)", texts)
        
        data = '\n'.join(conn.iterdump())
        
        logging.info("Writing to Database %s", database_path)
        with open(database_path, 'w') as f:
            f.write(data)
        
if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:\t%(message)s', level=logging.DEBUG)
    create_database("music")
    
    load_database()
    query(None)
    logging.info("Exiting")