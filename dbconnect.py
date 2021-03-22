# importing the library to connect with postgres
import psycopg2

# make a connection to the database, exchange dbname and user variables with the appropriate values 
conn = psycopg2.connect("dbname=postgres user=x")


cur = conn.cursor()

# this line executes the stored procedure 'storedProName()' 
cur.execute("CALL schema.storedProName();")

# if the executed query/stored procedure returns records, those can be acquired like this
records = cur.fetchall() 

# if any problem occured during execution, you can rollback like this
cur.execute("ROLLBACK")

# always commit, always! (after rollback included and especially if you don't want to lose any changes)
conn.commit()
