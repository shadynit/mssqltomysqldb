# mssqltomysqldb
update data from mssql to mysql



In this modified code, after fetching the records from MySQL, a new list transformed_records is created to gender the transformed data.
Gender values are mapped to the corresponding source types ('Female' or 'Male'). If the value is neither 0 nor 1, you can customize the behavior by providing a default value or handling it according to your requirements.
The transformed_records list is then used to execute the insert query with the updated Source_Type values. The rest of the code remains the same.
