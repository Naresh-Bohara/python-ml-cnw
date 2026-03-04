create database pythoncnw;
use pythoncnw;

create table departments(
dept_id int primary key auto_increment,
dept_name varchar(50)
);

create table employees(
emp_id int primary key auto_increment,
name varchar(50),
salary int,
dept_id int,
foreign key (dept_id) references departments (dept_id)
);

/*
Foreign key is a column in one table that refers to the primary key of the another table
It creates a relationship between the tables
*/

insert into departments(dept_name) values("Development");

select * from departments;

insert into departments(dept_name) values
("HR"), 
("Sales"), 
("Finance");

insert into employees(name, salary, dept_id) values ("Santosh", 120000, null);

insert into employees(name, salary, dept_id) values ("Naresh", 120000, 1),
("Rohan", 10000, 1),
("Harish", 30000, 2),
("Kailash", 70000, 4),
("Pawan", 40000, 3);

select * from employees;

-- Join is used to combine rows from two or more tables based on foreign key.
/*
syntax:
select columns 
from table1
join table2
on table1.column = table2.column;
*/

-- inner join: INNER JOIN returns only those records that have matching values in both tables based on a specified condition.
-- fetch employees name and department associated with employee 
select employees.name, departments.dept_name
from employees 
inner join departments 
on employees.dept_id = departments.dept_id;


-- Left join: return all rows from left and matching rows from right
select e.name, d.dept_name
from employees e
left join departments d
on e.dept_id = d.dept_id;

-- Right join: return all rows from right and matching rows from left
select e.name, d.dept_name
from employees e
right join departments d
on e.dept_id = d.dept_id;

/*
-- Full outer join: return all rows from both right and left tables
select e.name, d.dept_name
from employees e
full outer join departments d
on e.dept_id = d.dept_id;
*/

-- MySQL does not support FULL OUTER JOIN directly. It can be simulated by combining LEFT JOIN and RIGHT JOIN using UNION.
select e.name, d.dept_name
from employees e
left join departments d
on e.dept_id = d.dept_id
union
select e.name, d.dept_name
from employees e
right join departments d
on e.dept_id = d.dept_id;


-- count employees in each departments:
select d.dept_name, count(e.emp_id) as total_employees
from departments d
left join employees e
on d.dept_id = e.dept_id
group by d.dept_name;


-- show employees with salary>30000 and their departments:
select e.name, e.salary, d.dept_name
from employees e
inner join departments d
on e.dept_id = d.dept_id
where e.salary > 30000;

-- show employee name and salary along with department name
select e.name, e.salary, d.dept_name
from employees e
left join departments d
on e.dept_id = d.dept_id;

-- display department name and average salary of employees
select d.dept_name, avg(e.salary) as avg_salary
from departments d
left join employees e
on d.dept_id = e.dept_id
group by d.dept_name;

-- find maximum and minimum salary in each departments
select d.dept_name,
       max(e.salary) as max_salary,
       min(e.salary) as min_salary
from departments d
left join employees e
on d.dept_id = e.dept_id
group by d.dept_name;