#!/bin/bash

export MYSQL_USER="root"
export MYSQL_PASSWORD="root123."

# 单线程测试。测试做了什么。
mysqlslap -a -u$MYSQL_USER -p$MYSQL_PASSWORD
 
# 多线程测试。使用–concurrency来模拟并发连接。
mysqlslap -a -c 100 -u$MYSQL_USER -p$MYSQL_PASSWORD
 
# 迭代测试。用于需要多次执行测试得到平均值。
mysqlslap -a -i 10 -u$MYSQL_USER -p$MYSQL_PASSWORD
 
mysqlslap ---auto-generate-sql-add-autoincrement -a -u$MYSQL_USER -p$MYSQL_PASSWORD
mysqlslap -a --auto-generate-sql-load-type=read -u$MYSQL_USER -p$MYSQL_PASSWORD
mysqlslap -a --auto-generate-secondary-indexes=3 -u$MYSQL_USER -p$MYSQL_PASSWORD
mysqlslap -a --auto-generate-sql-write-number=1000 -u$MYSQL_USER -p$MYSQL_PASSWORD
mysqlslap --create-schema world -q "select count(*) from City" -u$MYSQL_USER -p$MYSQL_PASSWORD
mysqlslap -a -e innodb -u$MYSQL_USER -p$MYSQL_PASSWORD
mysqlslap -a --number-of-queries=10 -u$MYSQL_USER -p$MYSQL_PASSWORD
 
# 测试同时不同的存储引擎的性能进行对比：
mysqlslap -a --concurrency=50,100 --number-of-queries 1000 --iterations=5 --engine=myisam,innodb --debug-info -u$MYSQL_USER -p$MYSQL_PASSWORD
 
# 执行一次测试，分别50和100个并发，执行1000次总查询：
mysqlslap -a --concurrency=50,100 --number-of-queries 1000 --debug-info -u$MYSQL_USER -p$MYSQL_PASSWORD
 
# 50和100个并发分别得到一次测试结果(Benchmark)，并发数越多，执行完所有查询的时间越长。为了准确起见，可以多迭代测试几次:
mysqlslap -a --concurrency=50,100 --number-of-queries 1000 --iterations=5 --debug-info -u$MYSQL_USER -p$MYSQL_PASSWORD
