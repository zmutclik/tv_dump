#!/bin/bash
#######################################################################################################################
find . -type f -name ".env" -exec rm {} \;
find ./config -type f -name "initfile.sql" -exec rm {} \;
find ./config -type f -name "db.backup.cnf" -exec rm {} \;

cp ./files/samples/.env.sample .env
cp ./files/samples/initfile.sample.sql ./config/initfile.sql
cp ./files/samples/db.backup.cnf ./config/db.backup.cnf

#######################################################################################################################
export DBAPPUSERX       =$(curl --silent https://randomuser.me/api/ | jq '.results[].login.username')
export USERYBACKUPX     =userbackup_$(curl --silent https://randomuser.me/api/ | jq '.results[].login.username')

export DBROOTPASSWORDX  =$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
export DBAPPPASSWORDX   =$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)
export PASSYBACKUPX     =$(cat /dev/urandom | tr -dc 'a-zA-Z0-9' | fold -w 32 | head -n 1)

#######################################################################################################################
sed -i~ "/^DB_ROOTPASSWORD=/s/=.*/=$DBROOTPASSWORDX/" .env

sed -i~ "/^DB_APPUSER=/s/=.*/=$DBAPPUSERX/" .env
sed -i~ "/^DB_APPPASS=/s/=.*/=$DBAPPPASSWORDX/" .env

sed -i~ "/^DB_USERXBACKUP=/s/=.*/=$USERYBACKUPX/" .env
sed -i~ "/^DB_PASSXBACKUP=/s/=.*/=$PASSYBACKUPX/" .env

sed -i~ "/^RABBITMQ_USER=/s/=.*/=$RABBITMQUSER/" .env
sed -i~ "/^RABBITMQ_PASS=/s/=.*/=$RABBITMQPASS/" .env

sed -i 's/"//gI' .env

source .env

#######################################################################################################################
sed -i "s/DB_ROOTPASSWORD/$DBROOTPASSWORDX/gI"  ./config/initfile.sql
sed -i "s/DB_APPUSER/$DBAPPUSERX/gI"            ./config/initfile.sql
sed -i "s/DB_APPPASS/$DBAPPPASSWORDX/gI"        ./config/initfile.sql
sed -i "s/USERYBACKUPX/$USERYBACKUPX/gI"        ./config/initfile.sql
sed -i "s/PASSYBACKUPX/$PASSYBACKUPX/gI"        ./config/initfile.sql
sed -i "s/DB_NAME/$DB_NAME/gI"                  ./config/initfile.sql

sed -i 's/"//gI' ./config/initfile.sql

#######################################################################################################################
sed -i "s/USERYBACKUPX/$USERYBACKUPX/gI"        ./config/db.backup.cnf
sed -i "s/PASSYBACKUPX/$PASSYBACKUPX/gI"        ./config/db.backup.cnf

sed -i 's/"//gI' ./config/db.backup.cnf

#######################################################################################################################
rm .env~