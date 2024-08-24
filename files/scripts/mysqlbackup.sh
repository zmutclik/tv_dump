#!/bin/bash

MYSQL_ARGS="--defaults-extra-file=/root/.my.cnf"
MYSQL="/usr/bin/mysql $MYSQL_ARGS"
MYSQLDUMP="/usr/bin/mysqldump $MYSQL_ARGS"
BACKUP="/backups/mysql"

$MYSQL -BNe "show databases" | egrep -v '(mysql|.*_schema|sys)' | xargs -n1 -I {} $MYSQLDUMP {} -r $BACKUP/{}.sql > /dev/null 2>&1 
chmod 640 $BACKUP/*.sql
chgrp backup $BACKUP/*.sql