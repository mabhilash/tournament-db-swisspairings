-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

---CREATE DATABASE tournament;
/*CREATE TABLE players(id serial primary key,name varchar(100) not null );
CREATE TABLE matches(match_id serial primary key, winner integer references players(id), loser integer references players(id))

INSERT INTO players(name) VALUES('Abhilash');
INSERT INTO players(name) VALUES('Uday');
INSERT INTO players(name) VALUES('Chaitu');
INSERT INTO players(name) VALUES('Sravan');
INSERT INTO players(name) VALUES('JK');
INSERT INTO players(name) VALUES('Manoj');*/

---CREATE TABLE matches(match_id serial primary key, winner integer references players(id), loser integer references players(id))
/*
INSERT INTO matches(winner, loser) VALUES(1,5);
INSERT INTO matches(winner, loser) VALUES(4,3);*/


CREATE VIEW matches_played AS(SELECT id,name, count(m.winner) AS matches 
FROM players p LEFT JOIN matches m ON (p.id = m.winner OR p.id = m.loser) group by p.id);

CREATE VIEW matches_won AS(SELECT id,name, count(m.winner) AS wins 
FROM players p LEFT JOIN matches m ON (p.id = m.winner) group by p.id);

---SELECT m.id,m.name,m.matches,w.wins FROM matches_played JOIN matches_won ON m.id=w.id ORDER BY w.wins DESC;