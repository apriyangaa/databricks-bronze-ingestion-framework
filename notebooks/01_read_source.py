from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# Placeholder path 
SOURCE_PATH = "abfss://source@storage/account/hr/employee.csv"

df = (
    spark.read
    .option("header", True)
    .csv(SOURCE_PATH)
)

df.display()
