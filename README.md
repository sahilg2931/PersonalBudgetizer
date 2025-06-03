# PersonalBudgetizer

# DESIGN

# What is it ?? - >
Tool for personal finance budgeting and tracking and alerting.

# Features
The salary(income of money) is a monthly event and budgeting will be done on a monthly basis , but tracking is dynamic and alerting is daily/user set granularity.
The user can  categorize his/her spending in preset brackets(in future brackets can be added/removed as well).
The user upon creating categories will define monthly budget either in percentage or absolute , which should total to the total salary or income for the month. 
The other input will be transaction history (personal input bank statements for now).

# Problem Subdivision 
What are the granularities for all events -> transaction history input by user - weekly , budgeting and bracket proportion budgeting - monthly , tracking (same as transaction history input by user ) , alerting - not req as the tracking is not dynamic as of now.

What are the fixed categories -> FlatExpenditures (rent + maid + electricity + maintainence if any for flat) , ConvenienceExpenditures (clothes , new gadgets , shopping ,  anything for convenience , resupplying health and hygiene products , fuel , cabs ) , Food ( all food  and deliveries of same) , Investment (all investments done monthly), MiscExpenditures(anything that is apart from rest of categories , this spending has to be scrutinized/categorized) , IncomeRemainder (should reflect the balance of bank account)

% or absolute budget for categories( will be fixed as of now) -> 
FlatExpendituresBudget - 17,500(flat rent), 1500 (maid rent),  1200(electricty bill) , 1000 (drinking water + resupply for other cleaning ingredients), 
ConvenienceExpendituresBudget - 30,000 
InvestmentBudget - 50000 
UncategorizedExpenditures - 0 (there can be a bit of leeway)
IncomeRemainder ( Total - all expenditures and investment should be around 60000 )

Input for Transaction History - bank statements.


# Implementation details/limits
-need to set cohere api key in env  to run the main.py
-bank statements will be sent to cohere AI API and hence that is a data privacy issue ?? is it ??
-not many tokens are supported , so only one month bank statement is being processed
-a lot of payments are being uncategorized, so they have to be summarized

# TODO Priority Wise
- complete rest of the logic in main.py - done
- since a lot of payments are being uncategorized, summarize them in categories , maybe summarize payments for any category using LLM.  - done 
- find solution to adhering to token limit as sometimes not all rows in bank statements will be returned from llm response   
- ability to give multiple banks statements and merge the interpretation 
- ability to categorize existing data with extra info (for e.g. sagar is my brother and not uncategorized) ??
- validation for tasks done by llm using api from different llms??
- feature for moving expenditure from one category to another, so if I think in food there is some money that is supposed to be in convenience , I should be able to shift it.
- instead of path take the csv as input from user


