#import packages
import pandas as pd
from tableone import TableOne
import numpy as np
import matplotlib.pyplot as plt


#import dataset
df = pd.read_csv('https://health.data.ny.gov/resource/gnzp-ekau.csv')
df.shape
list(df)

#Tableone
columns = ['total_charges', 'total_costs','length_of_stay']
categorical = ['gender','race','ethnicity','type_of_admission']
groupby = ['type_of_admission']
labels = ['Admission_type']
mytable = TableOne(df, columns=columns, categorical=categorical, groupby=groupby, rename=labels, pval=False)
print(mytable.tabulate(tablefmt = "fancy_grid"))

##Total Costs
mean_total_costs = df['total_costs'].mean()
median_total_costs = df['total_costs'].median()
max_total_costs = df['total_costs'].max()
min_total_costs = df['total_costs'].min()
df['total_costs'].describe()

##Total Charges
mean_total_charges = df['total_charges'].mean()
median_total_charges = df['total_charges'].median()
max_total_charges = df['total_charges'].max()
min_total_charges = df['total_charges'].min()
df['total_charges'].describe()

## Facility Name Pie Chart
df['facility_name'].value_counts()
Facility = np.array([957, 33, 8, 2])
labels = ["Jones Memorial", "Cuba Memorial","Not Dislcosed", "Olean General"]
plt.pie(Facility, labels = labels)
plt.legend()
plt.show()

##Length of Stay
mean_los = df['length_of_stay'].mean()
median_los = df['length_of_stay'].median()
max_los = df['length_of_stay'].max()
min_los = df['length_of_stay'].min()
df['length_of_stay'].describe()

##Type of Admission Pie Chart
df['type_of_admission'].value_counts()
y = np.array([439, 251, 200, 110])
mylabels = ["Emergency", "Elective", "Newborn", "Urgent"]
plt.pie(y, labels = mylabels)
plt.legend(title = "Admission Types")
plt.show()

## Demographics Pie Chart
df['race'].value_counts()
Race = np.array([992, 7, 1])
labels = ["White", "Black/African American","Other Race"]
plt.pie(Race, labels = labels)
plt.legend()
plt.show()

## Age Pie Chart
df['age_group'].value_counts()
Ages = np.array([282, 223, 208, 169, 118])
labels = ["70+", "0-17", "50-69", "18-29", "30-49"]
plt.pie(Ages, labels = labels)
plt.legend(title = "Age Groups")
plt.show()

##Severity of Illness Bar Chart
df['apr_severity_of_illness_description'].value_counts()
Severity = ['Minor', 'Moderate','Major', 'Extreme']
Count = [445, 319, 200, 36]
plt.bar(Severity, Count)
plt.title('Severity of Illness of Hospital Discharges')
plt.xlabel('Severity of Illness')
plt.ylabel('Number of Patients')
plt.show()

##Payment Type Bar Chart
df['payment_typology_2'].value_counts()
Payment = ['Self-Pay','Medicare','Medicaid','Private Insurance','Blue Cross/Blue Shield']
y = [574, 130, 107, 99, 59, 8]
plt.bar(Payment, y)
plt.title('Payment Typology of Hospital Discharges')
plt.xlabel('Payment Type')
plt.ylabel('Number of Patients')
plt.show()

