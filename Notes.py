"""Notes
Key elements we need here is prices not necessarily description, should I find anomolies with 
quantity, that is outliers, df.Description analysis will be greatly beneficial to see if these
were indeed large purchases or large returns and of what good. After that I can keep them
as there isn't any clear relationship I can see to run a regression analysis.
Only descriptive analysis can be done here.
What if I try to find relationship between retention rate and amount of purchases? 
"""

"""What were the major influencers of a major uptick in sales in March 2011 and November 2011??
Check number of sales per country in both months. Who was buying more? Check lowest sales moths too.
If defference isn't quite large check months with the largest returns as well."""



######################FINDINGS##############################
"""November 2011 has the most amount of sales as expected but has the second largest amount of returns.
The anomoly seems to be in March 2011 where there are fewer sales and one of the least amount of returns
available. This suggests that there are outliers in the March data and will be examining further as to find out
what they are. Since UnitPrice for all goods has been fixed, this suggests outlier in quantity sold. Perhap one
single value.
Update: Yes there are outliers, but they are not easily detected. Even after filtering out using IQR, they are
mixed up with actual transactions. One detectable method is goods with all alphabetic StockCodes seem to be
errors. 'Amazon Fee' for over 17K or postage fee over 100K. It is hard to fish out what is real and what isn't
without full context but dropped anyway as they are suspicious transactions."""