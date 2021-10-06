DROP DATABASE if exits movies_examples;
CREATE DATABASE movies_example;
\c movies_example

CREATE TABLE movies
(
    id SERIAL PRIMARY KEY
    title NOT NULL
    release_year INTEGER
    runtime INTEGER
    rating TEXT
);

INSERT INTO movies(
    title, release_year, runtime, rating
)
VALUES
('Star War', 2005, 136, 'PG-13'),
("Avatar", 2010, 109, 'PG-13'),
('Black Panther', 2008, 111, 'PG-13'),
('Jurasic World', 2015, 124, 'PG-13');