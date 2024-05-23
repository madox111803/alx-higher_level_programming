-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE IF NOT EXISTS DATABASE hbtn_0d_usa;
CREATE IF NOT EXISTS TABLE hbtn_0d_usa.states (
	id INT DEFAULT NOT NULL UNIQUE PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
