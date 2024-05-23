-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
CREATE IF NOT EXISTS DATABASE hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE IF NOT EXISTS TABLE states (
	PRIMARY KEY (id),
	id INT DEFAULT NOT NULL UNIQUE,
	name VARCHAR(256) NOT NULL
);
