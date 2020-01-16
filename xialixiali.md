```postgreSQL
-- Database: xialixiali

-- DROP DATABASE xialixiali;

CREATE DATABASE xialixiali
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'Chinese (Simplified)_China.936'
    LC_CTYPE = 'Chinese (Simplified)_China.936'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;
	
CREATE TABLE Time(
	day date,
	primary key(day)
);
CREATE TABLE rank(
	day date,
	rank int not null,
	name varchar,
	href varchar,
	primary key(day,rank),
	foreign key (day) references Time
);
select * from Time
select * from rank
```