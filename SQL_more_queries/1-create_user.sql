-- Script create user_0d_1
-- 1-create_user.sql
CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY user_0d_1_pwd;
GRANTS ALL PRIVILEGES ON *.* TO user_0d_1@localhost;