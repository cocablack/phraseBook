import getopt				# args
import logging				# logging    
    
database_path = "sentiment.db"
links_path = "links.txt"
    
def query(json_data):
    """ TODO
    Queries for book recommendations based off of the json_data we receive from
    the user
    
    """
    
    result = {}
    result["data"] = "hello world"
    
    return result
    
def load_database():
    """ TODO
    returns a dictionary/sql database
    
    """
    
    with open(database_path, 'r') as f:
        for line in f:
            print(line)

    return {}
    
def create_database(inputfile):
    """ TODO
    creates a database with links to a text on every line
    
    """
    
    with open(inputfile, 'r') as f:
        for line in f:
            print(line)

    return 
    
if __name__ == "__main__":
    logging.basicConfig(format='%(levelname)s:\t%(message)s', level=logging.DEBUG)
    create_database(links_path)
    logging.info("Exiting")
    
if __name__ == "__main__":
    main(sys.argv[1:])