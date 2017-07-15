-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

CREATE TABLE players(id serial primary key,name varchar(100) not null );

CREATE TABLE matches(match_id serial primary key, winner integer references players(id), loser integer references players(id));

CREATE VIEW matches_played AS(SELECT id,name, count(m.winner) AS matches 
FROM players p LEFT JOIN matches m ON (p.id = m.winner OR p.id = m.loser) group by p.id);

CREATE VIEW matches_won AS(SELECT id,name, count(m.winner) AS wins 
FROM players p LEFT JOIN matches m ON (p.id = m.winner) group by p.id);

