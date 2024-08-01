from sqlalchemy import create_engine

# Define the connection string
DATABASE_URL = 'postgresql://username:password@localhost/dbname'

# Create an SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Print out the connection string for confirmation
print("SQLAlchemy Engine Created.")


from sqlalchemy import text

# Connect to the database
with engine.connect() as connection:
    # Example query
    query = text("SELECT * FROM your_table LIMIT 10;")
    result = connection.execute(query)
    
    # Print the results
    for row in result:
        print(row)
