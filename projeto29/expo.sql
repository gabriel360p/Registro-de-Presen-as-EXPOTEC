-- drop database expotec;
create database expotec;
use expotec;

create table matriculas(
matcodigo int primary key not null auto_increment,
matmatricula int,
matpessoa varchar(45)
);

create table presenca(
precodigoint int primary key not null auto_increment,
prematmatricula int,
prematpessoa varchar(45),
predata date
);

create table servidores(
sercodigo int primary key not null auto_increment,
sermatricula int,
serpessoa varchar(45)
);