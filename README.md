# CSE215-2021
1. install python
  
  a. sudo apt update
  
  b. sudo apt install python3.8

2. install neccessary packages and libraries 
  
  a. sudo apt install libpq-dev
  
  b. pip3 install psycopg2

3. create postgresql user (in this example the user name is x, change to whatever name you want)
  
  a. CREATE USER x;
  
  b. ALTER USER x WITH SUPERUSER;

4. alter the python script as needed (specify the user name, start creating schemas, tables, querying and much more)

5. run the python script

  a. python3 script.py
