import np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split, RandomizedSearchCV
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.ensemble import RandomForestRegressor, AdaBoostRegressor, GradientBoostingRegressor

file_name = 'sorted_flights.csv'
data = pd.read_csv(file_name)
df = pd.DataFrame(data)

# df.info()
nulls = df.isnull().sum()
# print(nulls)

df['Outbound Time'] = df['Outbound Time'].str.replace('+1', '')
df['Return Time'] = df['Return Time'].str.replace('+1', '')

out_time = df['Outbound Time'].str.split(' – ')
df['Outbound Departure'] = out_time.str[0]
df['Outbound Arrival'] = out_time.str[1]

outdep_split = df['Outbound Departure'].str.split(':')
df['Outbound Departure Hours'] = outdep_split.str[0]
df['Outbound Departure Minutes'] = outdep_split.str[1]

outarr_split = df['Outbound Arrival'].str.split(':')
df['Outbound Arrival Hours'] = outarr_split.str[0]
df['Outbound Arrival Minutes'] = outarr_split.str[1]
# return
ret_time = df['Return Time'].str.split(' – ')
df['Return Departure'] = ret_time.str[0]
df['Return Arrival'] = ret_time.str[1]

retdep_split = df['Return Departure'].str.split(':')
df['Return Departure Hours'] = retdep_split.str[0]
df['Return Departure Minutes'] = retdep_split.str[1]

retarr_split = df['Return Arrival'].str.split(':')
df['Return Arrival Hours'] = retarr_split.str[0]
df['Return Arrival Minutes'] = retarr_split.str[1]

# print(df['Outbound Arrival Hours'], df['Outbound Arrival Minutes'])
# print(df['Return Arrival Hours'], df['Return Arrival Minutes'])

df['Stops'].replace('direct', '0', inplace=True)
total_stops = df['Stops'].str.split(' ')
total_stops = total_stops.str[0]  # direct=0
# print(total_stops)

df['Outbound hours'] = df['Outbound hours'].str.split(' ')
df['Return hours'] = df['Return hours'].str.split(' ')

df['Outbound Travel Hours'] = df['Outbound hours'].str[0]
df['Outbound Travel Hours'] = df['Outbound Travel Hours'].str.split('h')
df['Outbound Travel Hours'] = df['Outbound Travel Hours'].str[0]
df['Outbound Travel Minutes'] = df['Outbound hours'].str[1]
df['Outbound Travel Minutes'] = df['Outbound Travel Minutes'].str.split('m')
df['Outbound Travel Minutes'] = df['Outbound Travel Minutes'].str[0]

df['Return Travel Hours'] = df['Return hours'].str[0]
df['Return Travel Hours'] = df['Return Travel Hours'].str.split('h')
df['Return Travel Hours'] = df['Return Travel Hours'].str[0]
df['Return Travel Minutes'] = df['Return hours'].str[1]
df['Return Travel Minutes'] = df['Return Travel Minutes'].str.split('m')
df['Return Travel Minutes'] = df['Return Travel Minutes'].str[0]

total_stops = total_stops.astype('int64')
df['Outbound Departure Hours'] = df['Outbound Departure Hours'].astype('int64')
df['Outbound Departure Minutes'] = df['Outbound Departure Minutes'].astype('int64')
df['Outbound Arrival Hours'] = df['Outbound Arrival Hours'].astype('int64')
df['Outbound Arrival Minutes'] = df['Outbound Arrival Minutes'].astype('int64')
df['Return Departure Hours'] = df['Return Departure Hours'].astype('int64')
df['Return Departure Minutes'] = df['Return Departure Minutes'].astype('int64')
df['Return Arrival Hours'] = df['Return Arrival Hours'].astype('int64')
df['Return Arrival Minutes'] = df['Return Arrival Minutes'].astype('int64')

df['Outbound Travel Hours'] = df['Outbound Travel Hours'].astype('int64')
df['Outbound Travel Minutes'] = df['Outbound Travel Minutes'].astype('int64')
df['Return Travel Hours'] = df['Return Travel Hours'].astype('int64')
df['Return Travel Minutes'] = df['Return Travel Minutes'].astype('int64')

df['Outbound Total Travel Time'] = df['Outbound Travel Hours'] * 60 + df['Outbound Travel Minutes']
df['Return Total Travel Time'] = df['Return Travel Hours'] * 60 + df['Return Travel Minutes']
# print(return_travel_mins)

numerical = [total_stops, df['Outbound Departure Hours'], df['Outbound Departure Minutes'],
             df['Outbound Arrival Hours'],
             df['Outbound Arrival Minutes'], df['Return Departure Hours'], df['Return Departure Minutes'],
             df['Return Arrival Hours'], df['Return Arrival Minutes'],
             df['Outbound Total Travel Time'], df['Return Total Travel Time']]

df = df.drop(['Outbound Time', 'Outbound hours', 'Return Time', 'Return hours', 'Stops'], axis=1)
df = df.drop(['Outbound Departure', 'Outbound Arrival', 'Return Departure', 'Return Arrival'], axis=1)
pd.set_option('display.max_columns', None)

plt.figure(figsize=(15,8))
sns.distplot(df['Price'])
# plt.savefig('distribution-flights.png')
# plt.show()


plt.figure(figsize = (18,18))
sns.heatmap(df.corr(),annot= True, cmap = "BuPu")
plt.savefig('correlation-flights.png')
# plt.show() #correlation

a=1
plt.figure(figsize=(20,45))
for i in numerical:
    plt.subplot(6,3,a)
    sns.scatterplot(x=i,y=df['Price'])
    plt.xticks(rotation=90)
    plt.tight_layout(pad=3.0)
    a=a+1
# plt.savefig('scatter-flights.png')
# plt.show()


figure,axis=plt.subplots(4, 4, figsize=(15,15))
k=0
for i in range(4):
    for j in range(4):
        if k<len(df.columns):
            axis[i, j].boxplot(df.iloc[:, k])
            axis[i, j].set_title(df.columns[k])
            k += 1
# plt.savefig('outliers-flights.png')
# plt.show() #outliers


df.skew(numeric_only=True)  # threshold +-1 / return total travel time skewed 1.25, return travel hours 1.24
df['Return Total Travel Time'] = np.log(df['Return Total Travel Time'])
df['Return Travel Hours'] = np.log(df['Return Travel Hours'])
# print(df.skew(numeric_only=True))

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

ds_x = df.drop('Price', axis=1)
y = df['Price']
dataset = sc.fit_transform(ds_x)
x = pd.DataFrame(dataset, columns=ds_x.columns)  # scaling
# print(x)

dt = DecisionTreeRegressor()
svr = SVR()
knn = KNeighborsRegressor()
lr = LinearRegression()
rfr = RandomForestRegressor()
ad = AdaBoostRegressor()
gd = GradientBoostingRegressor()

# x_train, x_test, y_train, y_test=train_test_split(x,y, test_size=0.3, random_state=42)
# for i in [dt,svr,knn,lr]:
#     i.fit(x_train,y_train)
#     pred=i.predict(x_test)
#     test_score=r2_score(y_test,pred)
#     train_score=r2_score(y_train,i.predict(x_train))
#     if abs(train_score-test_score)<=0.1:
#         print(i)
#         print('R2 score is ', r2_score(y_test,pred))
#         print('R2 for train data', r2_score(y_train,i.predict(x_train)))
#         print('Mean absolute error is ', mean_absolute_error(y_test, pred))
#         print('Mean squared error is ', mean_squared_error(y_test,pred))
#         print('Root mean squared error is ', (mean_squared_error(y_test,pred,squared=False)))

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
for i in [rfr, ad, gd]:
    i.fit(x_train, y_train)
    pred = i.predict(x_test)
    test_score = r2_score(y_test, pred)
    train_score = r2_score(y_train, i.predict(x_train))
    if abs(train_score - test_score) <= 0.2:
        print(i)
        print('r2 score is ', r2_score(y_test, pred))
        print('r2 for train data', r2_score(y_train, i.predict(x_train)))
        print('mean absolute error is ', mean_absolute_error(y_test, pred))
        print('mean squared error is ', mean_squared_error(y_test, pred))
        print('root mean squared error is ', (mean_squared_error(y_test, pred, squared=False)))

# GradientBoostingRegressor (gd) highest r2=0.74

y_train_pred = gd.predict(x_train)
y_test_pred = gd.predict(x_test)
plt.scatter(y_test,y_test_pred,alpha=0.2,color="DarkRed")
plt.title('Actual vs. Predicted Airline Prices')
plt.xlabel('Predicted Airline Prices')
plt.ylabel('Actual Airline Prices')
plt.savefig('final-model-flights.png')
plt.show()


table = pd.DataFrame({
    "Predicted Price" : gd.predict(x_test),
    "Actual Price" : y_test}).reset_index(drop = True)
table.to_csv(r'C:\Users\Alsu\Desktop\final-model.csv', index = False, header=True)
# print(table)


