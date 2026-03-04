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

-- adding new column in existing table:
alter table students_info add email varchar(30);

insert into students_info (id, name, age, address, email) values (1, "ram", 22, "ktm", "nam@gmail.com"),
(2, "shyam", 23, "dhn", "shyam@gmail.com");

-- viewing data 
select * from students_info;
select name, age, address from students_info;

desc students_info;

