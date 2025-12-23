from pyspark.sql.functions import col

# Mapping source column names to standardised names
COLUMN_MAPPING = {
    "EmployeeID": "employee_id",
    "FirstName": "first_name",
    "LastName": "last_name"
}

df_std = df

for source_col, target_col in COLUMN_MAPPING.items():
    if source_col in df_std.columns:
        df_std = df_std.withColumnRenamed(source_col, target_col)

df_std.display()
