create database customers;
show databases;
use customers;

create table customer_info(id integer,first_name varchar(255),last_name varchar(255),email varchar(255) );

select tables;

show databases;
show tables;

select * from customer_info;

insert into customer_info(id,first_name,last_name,email) value(1,"devesh","tripa","deve@gmail.com");
insert into customer_info values(2,"deves","tripathi","devesh@gmail.com"),(3,"dev","tripathi","deveshtripathi2202@gmail.com");

truncate table customer_info;

drop table customer_info;
show tables;
show databases;
drop database customers;