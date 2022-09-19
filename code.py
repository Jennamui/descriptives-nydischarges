#import packages
from pickletools import int4
import pandas as pd
from tableone import TableOne

#import dataset
df = pd.read_csv('data/Hospital_Inpatient_Discharges__SPARCS_De-Identified___2016.csv')
df.shape
list(df)

df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')
df['Total_Charges'] = df['Total_Charges'].astype(int)

#Tableone
columns = ['Total_Charges', 'Total_Costs','Length_of_Stay']
categorical = ['Gender','Race','Ethnicity','Type_of_Admission']
groupby = ['Type_of_Admission']
labels = ['Admission_type']
mytable = TableOne(df, columns=columns, categorical=categorical, groupby=groupby, rename=labels, pval=False)
print(mytable.tabulate(tablefmt = "fancy_grid"))

