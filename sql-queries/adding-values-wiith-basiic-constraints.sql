create table teachers (
id int,
name varchar(40) not null,
email varchar(50) not null,
salary int not null,
addresss varchar(50) 
);

select * from teachers;

alter table teachers
modify addresss varchar(50) not null;

insert into teachers(id, name, email, salary) values(1, "naresh", "n@gmail.com", 2000000);

create table users(
id int primary key auto_increment,
name varchar(40) not null,
email varchar(50) not null, 
age int check(age >= 18),
city varchar(50) default "ktm"
);

insert into users(name, email, age) values ("nari", "nari@gmail.com", 23);
select* from users;
desc table users;

/*
updating record 
syntax:
update table_name
set column = new_value1, cloumn2=new_value2
where condition
*/

update users set city = "pokhara", name="naresh"
where id = 1;

/*
deleting record
syntax:
delete from table_name
where condition;
*/

delete from users
where id = 2;

/*
create table ()
id primary key auto increment
name not null
age
marks > 40
city default ...
*/