# TodoList with Flask
>**python3, flask, jinja2
>mariadb, ubuntu16**

## 데이터베이스 세팅 (mysql_server)
user = root , passwd = '1234' 로 설정
<pre><code>
create database todo;
use todo;
</code><code>
create table todolist (
seq int auto_increment primary key,
userid varchar(50) not null,
priority varchar(20) default '0',
title varchar(50),
contain varchar(50),
deadline varchar(50),
idDone varchar(50));
</code><code>
create table users (
userid varchar(50) primary key
passwd varchar(50));
</code></pre>
