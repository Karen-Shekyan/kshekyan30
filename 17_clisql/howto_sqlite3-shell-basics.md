Scuba Doo Dog Erasers: Karen Shekyan, Gabriel Thompson, Russell Goychayev \
SoftDev \
K17: Shell Game \
2022-10-24 \
time spent: 0.5 hours

# qcc
- In the schema, what does `CREATE` mean?
- `.databases` should always print at least 2 databases, according to the documentation. We only got one.
- How do we write to databases using SQL?

# nota bene:
## creating tables
To create a new SQLite database named "ex1" with a single table named "tbl1", you might do this:
```
$ sqlite3 ex1
SQLite version 3.36.0 2021-06-18 18:36:39
Enter ".help" for usage hints.
sqlite> create table tbl1(one text, two int);
sqlite> insert into tbl1 values('hello!',10);
sqlite> insert into tbl1 values('goodbye', 20);
sqlite> select * from tbl1;
hello!|10
goodbye|20
sqlite>
```
- sql will autobox your table inputs. For example, the following code will not cause an error, even though tb1 wants (text, int)
```
insert into tbl1 values(1, 2);
```

## querying database
To see a list of tables:
```
.tables
```
To see a list of databases:
```
.databases
```
To see the schema (the structure) of a table:
```
.schema
```
These commands are shortcuts for things that can be done by other means.

## editing databases
```
.open databaseName
select * from table;
```
