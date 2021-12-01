# Databricks notebook source
# MAGIC %sql
# MAGIC CREATE TABLE students (name VARCHAR(64), address VARCHAR(64), student_id INT);
# MAGIC 
# MAGIC INSERT INTO students VALUES
# MAGIC     ('Amy Smith', '123 Park Ave, San Jose', 111111);

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO students VALUES
# MAGIC     ('Bob Brown', '456 Taylor St, Cupertino', 222222),
# MAGIC     ('Cathy Johnson', '789 Race Ave, Palo Alto', 333333);

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from students

# COMMAND ----------

