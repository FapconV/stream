import joblib 
import random
import pandas as pd
import statsmodels.api as sm


def Rand(start, end, num):
    res = []
 
    for j in range(num):
        num = random.randint(start, end)
        res.append(num)  
    return res
 
# Driver Code
num = 10000
start = 0
end = 500
data=Rand(start, end, num)

time=pd.date_range('17/10/2021', periods = 10000, freq ='H')
list_of_tuples = list(zip(time, data))
list_of_tuples 
df = pd.DataFrame(list_of_tuples,
                  columns = ['Time', 'Data'])
    
df.index=df.Time
df=df.drop(columns='Time')

fit = sm.tsa.statespace.SARIMAX(df.Data[9500:10000], order=(2, 1, 4),seasonal_order=(0,1,1,30)).fit()

joblib.dump(fit, './SARIMA.joblib')

