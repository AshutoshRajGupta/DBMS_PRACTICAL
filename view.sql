
/* Views in SQL are kind of virtual tables. A view also has rows and columns as they are in a real table in the database. 
We can create a view by selecting fields from one or more tables present in the database. A View can either have all the rows 
of a table or specific rows based on certain condition.*/

Enter password: ********
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 8
Server version: 8.0.29 MySQL Community Server - GPL

Copyright (c) 2000, 2022, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| computer_student   |
| employee           |
| information_schema |
| mysql              |
| performance_schema |
| student            |
| sys                |
+--------------------+
7 rows in set (0.03 sec)

mysql> use computer_student
Database changed
mysql> show tables;
+----------------------------+
| Tables_in_computer_student |
+----------------------------+
| employee                   |
| student_details            |
| students                   |
+----------------------------+
3 rows in set (0.02 sec)



mysql> show tables;
+----------------------------+
| Tables_in_computer_student |
+----------------------------+
| employee                   |
| student_details            |
+----------------------------+
2 rows in set (0.00 sec)

mysql> select * from employee;
+--------+----------+--------+------------+-----+
| Emp_id | Emp_name | city   | Emp_salary | age |
+--------+----------+--------+------------+-----+
|      1 | Aman     | nagpur |      12000 |  20 |
|      2 | Ashutosh | mumbai |      15000 |  21 |
+--------+----------+--------+------------+-----+
2 rows in set (0.02 sec)

mysql> insert into employee values(3,"Aryan","pune",20000,20),(4,"sarthak","nashik",18000,21);
Query OK, 2 rows affected (0.01 sec)
Records: 2  Duplicates: 0  Warnings: 0

mysql> select * from employee;
+--------+----------+--------+------------+-----+
| Emp_id | Emp_name | city   | Emp_salary | age |
+--------+----------+--------+------------+-----+
|      1 | Aman     | nagpur |      12000 |  20 |
|      2 | Ashutosh | mumbai |      15000 |  21 |
|      3 | Aryan    | pune   |      20000 |  20 |
|      4 | sarthak  | nashik |      18000 |  21 |
+--------+----------+--------+------------+-----+
4 rows in set (0.00 sec)

mysql> create table department (Emp_id int,Dname varchar(20));
Query OK, 0 rows affected (0.03 sec)

mysql> insert into department values(1,"Account"),(2,"sales"),(3,"Finance"),(4,"sales");
Query OK, 4 rows affected (0.01 sec)
Records: 4  Duplicates: 0  Warnings: 0

mysql> select * from department ;
+--------+---------+
| Emp_id | Dname   |
+--------+---------+
|      1 | Account |
|      2 | sales   |
|      3 | Finance |
|      4 | sales   |
+--------+---------+
4 rows in set (0.00 sec)

--creating a view 
mysql> CREATE view Emp_details as select Emp_id,Emp_name,city from employee;
Query OK, 0 rows affected (0.01 sec)

mysql> select * from Emp_details;
+--------+----------+--------+
| Emp_id | Emp_name | city   |
+--------+----------+--------+
|      1 | Aman     | nagpur |
|      2 | Ashutosh | mumbai |
|      3 | Aryan    | pune   |
|      4 | sarthak  | nashik |
+--------+----------+--------+
4 rows in set (0.00 sec)



mysql> create view Employeename as select Emp_id,Emp_name from employee;
Query OK, 0 rows affected (0.01 sec)

mysql> select * from Employeename;
+--------+----------+
| Emp_id | Emp_name |
+--------+----------+
|      1 | Aman     |
|      3 | Aryan    |
|      2 | Ashutosh |
|      4 | sarthak  |
+--------+----------+
4 rows in set (0.00 sec)

 --creating a view from two table

mysql> create view Employee_Depart_details as select employee.Emp_id,employee.Emp_name,department.Dname from employee,department 
       where employee.Emp_id=department.Emp_id;
Query OK, 0 rows affected (0.01 sec)

mysql> select * from Employee_Depart_details;
+--------+----------+---------+
| Emp_id | Emp_name | Dname   |
+--------+----------+---------+
|      1 | Aman     | Account |
|      2 | Ashutosh | sales   |
|      3 | Aryan    | Finance |
|      4 | sarthak  | sales   |
+--------+----------+---------+
4 rows in set (0.00 sec)

/*mysql> insert into Emp_details (Emp_id,Emp_name,city) values(5,"Akshay","pune");
ERROR 1423 (HY000): Field of view 'computer_student.emp_details' underlying table doesn't have a default value
mysql> insert into Emp_details (Emp_id,Emp_name,city)values(5,"Akshay","pune");
ERROR 1423 (HY000): Field of view 'computer_student.emp_details' underlying table doesn't have a default value*/

mysql> select * from Emp_details;
+--------+----------+--------+
| Emp_id | Emp_name | city   |
+--------+----------+--------+
|      1 | Aman     | nagpur |
|      2 | Ashutosh | mumbai |
|      3 | Aryan    | pune   |
|      4 | sarthak  | nashik |
+--------+----------+--------+
4 rows in set (0.00 sec)


--Alter command in view 
--Adding a column
mysql> Alter view Emp_details as select Emp_id,Emp_name,city,age from employee;
Query OK, 0 rows affected (0.01 sec)

mysql> select * from Emp_details;
+--------+----------+--------+-----+
| Emp_id | Emp_name | city   | age |
+--------+----------+--------+-----+
|      1 | Aman     | nagpur |  20 |
|      2 | Ashutosh | mumbai |  21 |
|      3 | Aryan    | pune   |  20 |
|      4 | sarthak  | nashik |  21 |
+--------+----------+--------+-----+
4 rows in set (0.00 sec)


--updating in view
mysql> update Emp_details set age=22 where Emp_name="Aryan";
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from Emp_details;
+--------+----------+--------+-----+
| Emp_id | Emp_name | city   | age |
+--------+----------+--------+-----+
|      1 | Aman     | nagpur |  20 |
|      2 | Ashutosh | mumbai |  21 |
|      3 | Aryan    | pune   |  22 |
|      4 | sarthak  | nashik |  21 |
+--------+----------+--------+-----+
4 rows in set (0.00 sec)


--delete command in view
mysql> delete from Emp_details where age=22;
Query OK, 1 row affected (0.01 sec)

mysql> select * from Emp_details;
+--------+----------+--------+-----+
| Emp_id | Emp_name | city   | age |
+--------+----------+--------+-----+
|      1 | Aman     | nagpur |  20 |
|      2 | Ashutosh | mumbai |  21 |
|      4 | sarthak  | nashik |  21 |
+--------+----------+--------+-----+
3 rows in set (0.00 sec)


--drop view
mysql> drop view Employee_Depart_details;
Query OK, 0 rows affected (0.01 sec)

mysql> select * from Employee_Depart_details;
ERROR 1146 (42S02): Table 'computer_student.employee_depart_details' doesn't exist


mysql> Alter view Emp_details as select Emp_id,Emp_name,city,age from employee rename  age to Emp_age;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'rename  age to Emp_age' at line 1
mysql> 
