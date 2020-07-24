# data-sets
Advertising dataset simulated from the idea of the Advertising.csv dataset in the book:  An Introduction to Statistical Learning with Applications in R
by Gareth James, Daniela Witten, Trevor Hastie and Robert Tibshirani, http://faculty.marshall.usc.edu/gareth-james/ISL/.
The dataset in the book has the shape (200, 4) with predictor variables as TV, Newspaper, Radio and target variable as Sales. All variables are given in terms of dollars.
There is a full discussion of the dataset in the book and the book and the dataset are both feely avaiable from the above url.
The current dataset has the shape (1796, 7). It was in the shape of (2000, 7) where after droping the outliers became (1796,7). The predictor variables are Internet, Email,
Blog, WebBanner, Promotional, SmartPhone and the target variable is Sales. The values of the predictors are the costs for advertising some products while the target value is
the amount of the money obtained by selling the products. 
---------------------------------------------------------------------------------------------------------------------------------------------------
Diet_Gym_Finance.txt dataset consists of three time series. To see the plot use the following code.

DGF = pd.read_csv('Diet_Gym_Finance.txt', parse_dates=['Month'], index_col='Month')
DGF.shape
DGF.head()
DGF.index

plt.plot(DGF.diet, color='red', label='Diet')
plt.plot(DGF.gym, color='blue', label='GYM')
plt.plot(DGF.finance, color='green', label='FINANCE')
plt.legend()
plt.show()
-------------------------------------------------------------------------------------------------------------------------------------------------------
churn dataset 
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('churn.csv')
m = df.groupby(['Churn']).mean()
m.plot(kind='bar')
#labels= ['no','yes']
plt.xlabel('Churn', size=20)
plt.ylabel('Counts', size=20)
plt.title('CHURN MEAN', size=20)
plt.legend(loc=1)
---------------------------------------------------------------------------------------------------------------------------------------------------------
https://en.wikipedia.org/wiki/Anscombe%27s_quartet

Anscombe's quartet comprises four data sets that have nearly identical simple descriptive statistics, yet have very different distributions and appear very different when graphed. Each dataset consists of eleven (x,y) points. They were constructed in 1973 by the statistician Francis Anscombe to demonstrate both the importance of graphing data before analyzing it and the effect of outliers and other influential observations on statistical properties. He described the article as being intended to counter the impression among statisticians that "numerical calculations are exact, but graphs are rough."[1]



