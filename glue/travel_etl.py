from pyspark.context import SparkContext
from awsglue.context import GlueContext

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

df = spark.read.json("s3://travel-data-lake/raw/")

df.write.mode("overwrite").option("header","true").csv("s3://travel-data-lake/processed/")