import pyspark
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import SQLContext
import json
from pyspark.sql.functions import mean, min, max
from pyspark.sql import SparkSession
import matplotlib.pyplot as plt

spark = SparkSession.builder.appName("MinhaAplicacao").getOrCreate()
sc = spark.sparkContext
sqlContext = pyspark.SQLContext(sc)

df= spark.read.json('../yelp_academic_dataset_review.json')

df_baa = df.filter(df['business_id'] == '--9e1ONYQuAa-CB_Rrw7Tw').select('stars','date') # Separa o df com somente o business de intresse
df_baaY = df_baa.withColumn("year_only",(trunc(df_baa.date, 'year'))) 

df_baaY = df_baaY.withColumn("date_only",to_date(col("date"))) # tira as horas minutos e segundos para poder dar o groupBy
df_baaY = df_baaY.orderBy(unix_timestamp("year_only", "yyyy-mm-dd"))

df_baaY1 = df_baaY.filter(df['stars'] == 1).select('stars','year_only') 
df_baaY1 = df_baaY1.groupBy('year_only').count()
df_baaY1 = df_baaY1.select(col("year_only"), col("count").alias("count_stars"))
df_baaY1 = df_baaY1.orderBy(unix_timestamp("year_only", "yyyy-mm-dd"))

df_baaY2 = df_baaY.filter(df['stars'] == 2).select('stars','year_only') 
df_baaY2 = df_baaY2.groupBy('year_only').count()
df_baaY2 = df_baaY2.select(col("year_only"), col("count").alias("count_stars"))
df_baaY2 = df_baaY2.orderBy(unix_timestamp("year_only", "yyyy-mm-dd"))

df_baaY3 = df_baaY.filter(df['stars'] == 3).select('stars','year_only') 
df_baaY3 = df_baaY3.groupBy('year_only').count()
df_baaY3 = df_baaY3.select(col("year_only"), col("count").alias("count_stars"))
df_baaY3 = df_baaY3.orderBy(unix_timestamp("year_only", "yyyy-mm-dd"))

df_baaY4 = df_baaY.filter(df['stars'] == 4).select('stars','year_only') 
df_baaY4 = df_baaY4.groupBy('year_only').count()
df_baaY4 = df_baaY4.select(col("year_only"), col("count").alias("count_stars"))
df_baaY4 = df_baaY4.orderBy(unix_timestamp("year_only", "yyyy-mm-dd"))

df_baaY5 = df_baaY.filter(df['stars'] == 5).select('stars','year_only') 
df_baaY5 = df_baaY5.groupBy('year_only').count()
df_baaY5 = df_baaY5.select(col("year_only"), col("count").alias("count_stars"))
df_baaY5 = df_baaY5.orderBy(unix_timestamp("year_only", "yyyy-mm-dd"))

y_ans_val1 = [val.count_stars for val in df_baaY1.select('count_stars').collect()]
x_ts1 = [val.year_only for val in df_baaY1.select('year_only').collect()]
#plt.plot(x_ts, y_ans_val,label='1 star')

y_ans_val2 = [val.count_stars for val in df_baaY2.select('count_stars').collect()]
x_ts2 = [val.year_only for val in df_baaY2.select('year_only').collect()]
#plt.plot(x_ts, y_ans_val,label='2 stars')

y_ans_val3 = [val.count_stars for val in df_baaY3.select('count_stars').collect()]
x_ts3 = [val.year_only for val in df_baaY3.select('year_only').collect()]
#plt.plot(x_ts, y_ans_val,label='3 stars')

y_ans_val4 = [val.count_stars for val in df_baaY4.select('count_stars').collect()]
x_ts4 = [val.year_only for val in df_baaY4.select('year_only').collect()]
#plt.plot(x_ts, y_ans_val,label='4 stars')

y_ans_val5 = [val.count_stars for val in df_baaY5.select('count_stars').collect()]
x_ts5 = [val.year_only for val in df_baaY5.select('year_only').collect()]

plt.plot(x_ts1, y_ans_val1,x_ts2, y_ans_val2,x_ts3, y_ans_val3,x_ts4, y_ans_val4,x_ts5, y_ans_val5)
plt.gca().legend(('1 star','2 stars','3 stars','4 stars','5 stars'))

plt.show()