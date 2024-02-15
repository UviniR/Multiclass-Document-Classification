# read the files
from pyspark.sql import SparkSession
import types
import pandas as pd
from pyspark import SparkContext 
sc = SparkContext.getOrCreate() 
spark = SparkSession.builder.getOrCreate()

# read alal the text files under intervention area
dataset = sc.wholeTextFiles("Data Set/Child Protection")


# split the text file name using .
dataset1 = dataset.map(
   lambda tuple: ((tuple[0].split("/")[-1]).split(".", 1)[0], 
                  (tuple[0].split("/")[-1]).split(".", 1)[1],tuple[1])
    )


# we can create a DataFrame so we can use SQL to manipulate the data
from pyspark.sql.types import *

classNameContent = StructType([StructField("fileclass", StringType(), True),
                               StructField("filename",  StringType(), True),
                               StructField("content",   StringType(), True)])
FinalDataSet = spark.createDataFrame(dataset1, classNameContent)

print("Total number of articles: " + str(FinalDataSet.count()) )

# write the dat into a data frame
df = FinalDataSet.toPandas()

df.to_csv ('Data Set/Upskilling.csv', index=False)