-- To create database:
CREATE database python;
use python;
/*
int varchar(n), char(n), float, date, boolean
*/

/*
To  create table
create table table_name(
column datatype,
................
................product
)
*/

create table students (
id int,
name varchar(50),
age int, 
city varchar(50)
);

/*
-- delete table
drop table students;
*/

/*
-- delete column
ALTER TABLE students
DROP COLUMN age;
*/

/*
delete table
drop database python;
*/

/* rename column
alter table students
change city address varchar(40)
*/

alter table students
change city address varchar(40);

-- rename table:
rename table students to students_info;