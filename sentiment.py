import getopt				# args
import logging				# logging    
import sqlite3
import os
from json import dumps

from textblob import TextBlob
from media_analysis import analysis
    
database_path = "sentiment.db"
    
conn = None
cur = None
result = None

logging.basicConfig(format='%(levelname)s:\t%(message)s', level=logging.DEBUG)

def query(json_data):
    """ TODO
    Queries for book recommendations based off of the json_data we receive from
    the user
    
    """
    logging.info("Query")
    
    print(json_data["text"])

    # print(result)

    return dumps(result[0])
    
def create_database(media_type):
    global result
    result = analysis(media_type) 

    # global conn
    # conn = sqlite3.connect(':memory:')
    # cur = conn.cursor()
        
    # cur.execute("DROP TABLE IF EXISTS Texts")
    # cur.execute("CREATE TABLE Texts(Media TEXT, \
    #     Id INT, Title TEXT, Author TEXT, Link TEXT, \
    #     Sentiment INT, Common TEXT)")        

    # cur.executemany("INSERT INTO Texts VALUES(?, ?, ?, ?, ?, ?, ?)", result)

if __name__ == "__main__":
    # create_database("music")
    # query(None)
    logging.info("Exiting")