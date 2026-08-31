import duckdb


# Connect to DuckDB database
connection = duckdb.connect("data/github.duckdb")


# Create a table called repositories
# and load data from the Parquet file
connection.execute("""
    CREATE OR REPLACE TABLE repositories AS
    SELECT *
    FROM read_parquet('data/processed/repositories.parquet')
""")


# Count total repositories
result = connection.execute("""
    SELECT COUNT(*)
    FROM repositories
""").fetchone()


print("Data loaded successfully into DuckDB!")
print("Total repositories:", result[0])


# Close database connection
connection.close()