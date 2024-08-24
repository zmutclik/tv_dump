-- CREATE USER IF NOT EXISTS root@localhost IDENTIFIED BY 'DB_ROOTPASSWORD';
-- SET PASSWORD FOR root@localhost = PASSWORD('DB_ROOTPASSWORD');
-- GRANT ALL ON *.* TO root@localhost WITH GRANT OPTION;

CREATE USER IF NOT EXISTS root@'%' IDENTIFIED BY 'DB_ROOTPASSWORD';
SET PASSWORD FOR root@'%' = PASSWORD('DB_ROOTPASSWORD');
GRANT ALL ON *.* TO root@'%' WITH GRANT OPTION;

CREATE USER IF NOT EXISTS USERYBACKUPX@localhost IDENTIFIED BY 'PASSYBACKUPX';
SET PASSWORD FOR USERYBACKUPX@localhost = PASSWORD('PASSYBACKUPX');
GRANT ALL ON *.* TO USERYBACKUPX@localhost WITH GRANT OPTION;

CREATE USER IF NOT EXISTS DB_APPUSER@'%' IDENTIFIED BY 'DB_APPPASS';
SET PASSWORD FOR DB_APPUSER@'%' = PASSWORD('DB_APPPASS');

CREATE DATABASE IF NOT EXISTS DB_NAME;
GRANT ALL ON DB_NAME.* TO DB_APPUSER@'%';