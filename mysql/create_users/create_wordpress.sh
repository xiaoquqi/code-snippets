#!/bin/bash
 
CREATE DATABASE IF NOT EXISTS wordpress default charset utf8 COLLATE utf8_general_ci;
GRANT ALL PRIVILEGES ON wordpress.* TO wordpressuser@"%" identified by 'password';
GRANT ALL PRIVILEGES ON wordpress.* TO wordpressuser@"localhost" identified by 'password';
FLUSH PRIVILEGES;
