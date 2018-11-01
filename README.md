# TodoList with Flask
__로컬 환경에서 실행__
>**python3, flask, jinja2
>mariadb, ubuntu16**

### 데이터베이스 세팅 (mysql_server)
>**user = root , passwd = '1234' 로 설정**
<pre><code>create database todo;
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
### 실행환경 세팅 (python3)
>**src/FlaskApp/requirements.txt 의 모듈 설치**
<pre><code>pip3 install -r requirements.txt
</code></pre>
>**FlaskApp 폴더의 run.py 실행**
<pre><code>python3 install run.py
</code></pre>
>**백그라운드에서 실행**
<pre><code>python3 install run.py &</code> 혹은
<code>nohup python3 install run.py &</code>
</pre>
