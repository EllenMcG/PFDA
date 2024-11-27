-- pfda database 
create database pfda;

--use pfda and create student table
use pfda;
create table student (id int, firstname varchar(100), age int(3));
insert into student (id, firstname, age) values (1,'joe',56);

--view data
select * from student;

--view columns
desc student;

--update data
update student set firstname='mary' where id = 1;

--delete data
Delete from student where id = 1;

-- drop student table
drop table student;

--create book table
create table book (id int, title varchar(250), author varchar(250), price decimal(4,2) NOT NULL);

--Insert data into book
insert into book (id, title, author, price) values (1,'Horns', 'Joe Hill',10.33);
insert into book (id, title, author, price) values (2,'The Stand', 'Stephen King',10.30);
insert into book (id, title, author, price) values (3,'Tress of the Emerald Sea', 'Brandon Sanderson',9.37);
insert into book (id, title, author, price) values (4,'Forth Wing', 'Rebecca Yarros',5.50);

--View data in book table
select * from book;

--View column types in book
desc book;