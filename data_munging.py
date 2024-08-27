import pandas as pd
import sqlite3

# Load the data
df0 = pd.read_csv('data/shipping_data_0.csv')
df1 = pd.read_csv('data/shipping_data_1.csv')
df2 = pd.read_csv('data/shipping_data_2.csv')

# Print the column names to ensure they are as expected
print("Columns in df0:", df0.columns)
print("Columns in df1:", df1.columns)
print("Columns in df2:", df2.columns)

# Merge df1 and df2 on 'shipment_identifier'
df_merged = pd.merge(df1, df2, on='shipment_identifier')

# Print the first few rows of the merged dataframe to verify
print("Merged dataframe preview:")
print(df_merged.head())

# Create a SQLite connection
conn = sqlite3.connect('shipment_database.db')

# Insert df0 directly into the database
df0.to_sql('shipping_data_0', conn, if_exists='replace', index=False)

# Insert the merged data into the database
df_merged.to_sql('shipping_data_merged', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

print("Data has been successfully inserted into the database.")
