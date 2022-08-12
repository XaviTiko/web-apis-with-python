import sqlite3 as SQL


def match_exact(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for an exact match
    3. If success return the definition
    4. If not return an empty list
    """
    db = SQL.connect( "data/dictionary.db" )
 
    # Query the database for exact matches
    sql_query = "SELECT * from entries WHERE word=?"
    match = db.execute(sql_query, (word,)).fetchall()
 
    # Close the connection to the database
    db.close()
 
 # Return the results
    return match
    # TODO: Establish connection to the dictionary database

    # TODO: Query the database for exact matches

    # TODO: Clone the connection to the database
    

    # Return the results
    return "TODO"


def match_like(word: str) -> list:
    """
    This method will:
    1. Accept a string
    2. Search the dictionary for approximate matches
    3. If success return the definition as a list
    4. If not return an empty list
    """
    db = SQL.connect( "data/dictionary.db" )
 # Query the database for exact matches
    sql_query = "SELECT * from entries WHERE word LIKE ?"
    match = db.execute(sql_query, ( "%" + word + "%" ,)).fetchall()
 # Clone the connection to the database
    db.close()
    return match
 # Return the re
    # TODO: Establish connection to the dictionary database
    
    # TODO: Query the database for exact matches
    
    # TODO: Clone the connection to the database
    
    # Return the results

