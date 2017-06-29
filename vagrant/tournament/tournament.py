#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    db = connect()
    conn = db.cursor()
    conn.execute("DELETE FROM matches")
    db.commit()
    db.close()
    
    """Remove all the match records from the database."""


def deletePlayers():
    db = connect()
    conn = db.cursor()
    conn.execute("DELETE FROM players")
    db.commit()
    db.close()

    """Remove all the player records from the database."""


def countPlayers():
    db = connect()
    conn = db.cursor()
    conn.execute("SELECT count(*) FROM players")
    count=conn.fetchone()[0]
    print count
    return count
    """Returns the number of players currently registered."""


def registerPlayer(name):
    db = connect()
    conn = db.cursor()
    conn.execute("INSERT INTO players(name) VALUES(%s)",(name,))
    db.commit()
    db.close()
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """


def playerStandings():
    db = connect()
    conn = db.cursor()
    conn.execute("SELECT m.id,m.name,w.wins,m.matches FROM matches_played m JOIN matches_won w ON m.id=w.id ORDER BY w.wins DESC")
    result = conn.fetchall()
    return result
    # count=0
    # for row in result:
    #     count=count+1
    #     print row
    # db.commit()
    # db.close()
    # return count

    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """


def reportMatch(winner, loser):
    db = connect()
    conn=db.cursor()
    conn.execute("INSERT into matches(winner,loser) VALUES(%s,%s)",(winner,loser,))
    db.commit()
    db.close()

    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """


