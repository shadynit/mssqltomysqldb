import pymysql
import pyodbc

# Connect to the  MySQL database
source_connection = pymysql.connect(
    host='hostip',
    user='username',
    password='Password',
    database='sourcedbname'
)

# Connect to the CIC_Customer MS SQL database
destination_connection = pyodbc.connect(
    'DRIVER={SQL Server};'
        'SERVER=hostip;'
        'DATABASE=destdbname;'
        'UID=username;'
        'PWD=Password;'
)
# Retrieve the data from the source data
select_query = '''
    SELECT id, column1, column2
           
    FROM source_table
    WHERE date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY)
'''

with source_connection.cursor() as source_cursor:
    # Execute the select query
    source_cursor.execute(select_query)
    
    # Fetch all the selected records
    records = source_cursor.fetchall()

# Transform the column2 values to 'Male' or 'Female'
transformed_records = []
for record in records:
    # Get the column2 value
    gender_type = record[8]
    
    # Map the gender_type to the desired values
    if gender_type == 0:
        source_type = 'female'
    elif gender_type == 1:
        source_type = 'male'
    else:
        # Handle any other cases or provide a default value
        source_type = 'Unknown'
    
    # Create a new record with the transformed source_type
    transformed_record = list(record)
    transformed_record[8] = source_type
    
    transformed_records.append(transformed_record)

# Insert the data into the destimation_table table in destdbname
insert_query = '''
    INSERT INTO dbo.destimation_table (dest_id, dest_column1, dest_column2,)
    VALUES (?, ?, ?)
'''

with destination_connection.cursor() as dest_cursor:
    # Iterate over the transformed records
    for record in transformed_records:
        # Execute the insert query for each record
        dest_cursor.execute(insert_query, record)
    
    # Commit the changes
    destination_connection.commit()

# Close the connections
source_connection.close()
destination_connection.close()

print ("Done")
