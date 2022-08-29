# Databricks notebook source
from my_lib.my_funcs import *

# COMMAND ----------

# MAGIC %md
# MAGIC The remainder of this notebook demonstrates using the functions declared in the referenced `my_funcs` Python file.

# COMMAND ----------

import numpy as np
import pandas as pd

Fdf = pd.DataFrame(np.random.normal(55, 25, 10000), columns=["temp"])
Fdf["unit"] = "F"

Cdf = pd.DataFrame(np.random.normal(10, 10, 10000), columns=["temp"])
Cdf["unit"] = "C"

df = spark.createDataFrame(pd.concat([Fdf, Cdf]))

display(df)

# COMMAND ----------

display(df.select(roundedTemp("unit", "temp")))

# COMMAND ----------

display(df.select(convertFtoC("unit", "temp")))

# COMMAND ----------

# MAGIC %md
# MAGIC ## Adding a cell

# COMMAND ----------


