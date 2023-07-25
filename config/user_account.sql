DROP TABLE IF EXISTS simple_login;

CREATE TABLE simple_login (
  id serial PRIMARY KEY,
  first_name varchar(30) NOT NULL,
  last_name varchar(30) NOT NULL,
  username varchar(30) UNIQUE NOT NULL,
  password varchar(100) NOT NULL,
  date DATE NOT NULL,
  created_at TIMESTAMP NOT NULL,
  updated_at TIMESTAMP NOT NULL
);
