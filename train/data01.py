import pandas as pd
import numpy as np

df = pd.read_csv('/home/lkit/Documents/Course/Big Data/Proj01/Dataset/test_samples.csv', header=None)
df.columns = ['pregnant','glucose','blood','skin','insulin','BMI','disbetes','age']
print(df)
data=df.as_matrix()
# (df[(df.glucose>120) & (df.blood>85)])[['glucose','blood']]
data[0][3]





