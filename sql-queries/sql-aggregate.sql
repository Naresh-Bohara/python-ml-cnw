create table employee(
id int primary key auto_increment,
name varchar(40) not null,
age int not null,
salary int check(salary>=10000) not null,
city varchar(40) not null default "dhangadhi"
);

insert into employee(name, age, salary, city) values("Naresh", 23, 11000, "dhangadhi");
insert into employee(name, age, salary, city) values("chahana", 20, 94000, "butwal" );

select * from employee;

/*
- Aggregate functions (count(), sum(), avg(), min(), max()
- count(): count no.of rows
*/

select count(*) from employee where name="santosh";
select sum(salary) from employee where city="dhangadhi";
select avg(age) from employee;
select min(salary) from employee;

select name, salary, city from employee where salary = (select min(salary) from employee);

select name, salary, city from employee where salary = (select max(salary) from employee);

select name, salary, city from employee where salary = (select min(salary) from employee)
OR salary = (select max(salary) from employee);
