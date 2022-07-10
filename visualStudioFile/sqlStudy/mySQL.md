## MySQL



## 安装mysql
下载地址 https://dev.mysql.com/downloads/mysql/  mysql-8.0.29-winx64
查看版本
mysql -v
解压后在根目录新建my.ini配置文件，并输入如下内容
```
[client]
# 设置mysql客户端默认字符集
default-character-set=utf8
[mysqld]
# 设置3306端口
port = 3306

# 设置mysql的安装目录
basedir=D:\\Program Files\\mysql-8.0.29-winx64

# 设置 mysql数据库的数据的存放目录，MySQL 8+ 不需要以下配置，系统自己生成即可，否则有可能报错
# datadir=C:\\Program Files\\mysql8

# 允许最大连接数
max_connections=20

# 服务端使用的字符集默认为8比特编码的latin1字符集
character-set-server=utf8

# 创建新表时将使用的默认存储引擎
default-storage-engine=INNODB
```
初始化数据库;
mysqld --initialize --console
执行完成后，会打印root的初始密码如： d000000
用管理员输入以下安装命令：
mysqld install
启动输入以下命令即可：net start mysql

## 启动与关闭
mysqld --console   
mysqladmin -uroot shutdown

cd /usr/bin
./mysqld_safe &
mysqladmin -uroot shutdown

## 查询用户信息
`SELECT host,user,password FROM user;`

show DATABASES;展示所有数据库

use mysql;使用数据库

show TABLES;展示所有表

show COLUMNS from func;从某表展示列

show index from user;展示索引

CREATE DATABASE 数据库名;创建数据库

DROP DATABASE 数据库名;删除数据库

导出表数据到指定目录
select * from user into OUTFILE "C:\\Users\\29545\\Desktop\\new\\3.txt"
查看导出安全选项
（1）secure_file_prive=null，限制mysqld 不允许导入导出
（2）secure_file_priv=/var/lib/mysql-files/，限制mysqld的导入导出只能发生在/var/lib/mysql-files/目录下
（3）secure_file_priv=' '，不对mysqld的导入导出做限制
show VARIABLES like '%secure_%'

## 常见增删改查命令  
## UNSIGEND 数据不重复 PRIMARY KEY 主键 ENGINE 存储引擎 DEFAULT CHARSET 设置编码 IF NOT EXISTS 不存在则创建
CREATE TABLE IF NOT EXISTS table_name(
column_name1 column_type1 UNSIGEND not null AUTO_INCREMENT,
column_name2 column_type2 default "1",
PRIMARY KEY(column_name1)
) ENGINE = InnoDB DEFAULT CHARSET = utf8;

## 删除表
DROP TABLE table_name;

## 添加字段 修改字段 删除字段
ALTER TABLE table_name ADD field_name field_type;
ALTER TABLE table_name CHANGE old_field_name new_field_name new_field_type;
ALTER TABLE table_name DROP field_name;

## 基础查询 条件查询 查询重命名
SELECT * FROM table_name;
SELECT field1 AS name1, ... fieldN AS nameN FROM table_name table_name1 WHERE CONDITION1 [AND | OR] CONDITION2;

朱子升 法律助理 ID:21418700, 15951738662，430302199801174511
程静 法律总监 ID:21418693, 13828869431，131181198504143540










