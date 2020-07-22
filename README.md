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




