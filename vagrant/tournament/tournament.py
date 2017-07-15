#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import random


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    conn = db.cursor()
    conn.execute("DELETE FROM matches")
    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    conn = db.cursor()
    conn.execute("DELETE FROM players")
    db.commit()
    db.close()


def countPlayers():
    """Returns the number of players currently registered."""
    db = connect()
    conn = db.cursor()
    conn.execute("SELECT count(*) FROM players")
    count = conn.fetchone()[0]
    return count


def registerPlayer(name):
    """Adds a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    conn = db.cursor()
    conn.execute("INSERT INTO players(name) VALUES(%s)", (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    conn = db.cursor()
    conn.execute("SELECT m.id,m.name,w.wins,m.matches FROM matches_played m"
                 " JOIN matches_won w ON m.id=w.id ORDER BY w.wins DESC")
    result = conn.fetchall()
    return result


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    conn = db.cursor()
    conn.execute("INSERT into matches(winner,loser)"
                 " VALUES(%s,%s)", (winner, loser,))
    db.commit()
    db.close()


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
<<<<<<< HEAD
    standings = playerStandings()
    matches = [row[3] for row in standings]
    pairings = []
    pairings = generatepairings(standings, pairings)
    return pairings


def generatepairings(standings, pairings):
    """This method generate all the possible pairs and returns the pairs list"""
    for i in range(0, len(standings), 2):
        for j in range(i+1, len(standings)):
            is_rematch = check_rematch(standings[i][0], standings[j][0])
            if is_rematch:
                continue
            else:
                while j > i+1:
                    temp = standings[j-1]
                    standings[j-1] = standings[j]
                    standings[j] = temp
                    j = j-1
                break
        pairings.append((standings[i][0], standings[i][1], standings[j][0],
                        standings[j][1]))
    return pairings


def check_rematch(id1, id2):
    """This method checks if two paired players have already played before"""
    db = connect()
    conn = db.cursor()
    conn.execute("SELECT count(*) from matches where winner=%s AND loser=%s OR"
                 " winner=%s AND loser=%s", (id1, id2, id2, id1, ))
    count = conn.fetchone()[0]
    db.commit()
    db.close()
    if count > 0:
        return True
    else:
        return False
||||||| merged common ancestors


=======
    standings = playerStandings()
    matches = [row[3] for row in standings]
    pairings = []
    pairings = generatepairings(standings, pairings)
    return pairings


def generatepairings(standings, pairings):
    for i in range(0, len(standings), 2):
        for j in range(i+1, len(standings)):
            is_rematch = check_rematch(standings[i][0], standings[j][0])
            if is_rematch:
                continue
            else:
                while j > i+1:
                    temp = standings[j-1]
                    standings[j-1] = standings[j]
                    standings[j] = temp
                    j = j-1
                break
        pairings.append((standings[i][0], standings[i][1], standings[j][0],
                        standings[j][1]))
    return pairings


def check_rematch(id1, id2):
    db = connect()
    conn = db.cursor()
    conn.execute("SELECT count(*) from matches where winner=%s AND loser=%s OR"
                 " winner=%s AND loser=%s", (id1, id2, id2, id1, ))
    count = conn.fetchone()[0]
    db.commit()
    db.close()
    if count > 0:
        return True
    else:
        return False
>>>>>>> cf4c6f2aa31f4955e2a95e6786c61be965e3c848
