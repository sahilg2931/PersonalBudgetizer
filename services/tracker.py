# models for tracking and summarizing month wise budget and expenditure.
from models.category import Category
from models.transaction import Transaction
import os
import csv


# Data of Budget Vs Expenditure for user predefined categories per month 
# updated via list of Object Transaction which is in turn interpreted 
# from bank statement
# there is one to one mapping in this from month to MonthBudgetTracker
class BudgetTracker:
    def __init__(self, monthly_budget): # TODO monthly budget should be unique to month
        self.monthly_budget = monthly_budget
        self.BudgetAndExpenditures={}

    def updateBudgetTracker(self, transactions):
         for t in transactions:
              transactionMonth = t.date.month
              transactionYear  = t.date.year 
              key = (transactionYear, transactionMonth)
              if key not in self.BudgetAndExpenditures:
                monthBudgetTracker = MonthBudgetTracker(transactionYear, transactionMonth, self.monthly_budget)
                monthBudgetTracker.updateMonthBudgettracker(t)
                self.BudgetAndExpenditures[key] = monthBudgetTracker
              else:
                existingMonthBudgetTracker = self.BudgetAndExpenditures[key]
                existingMonthBudgetTracker.updateMonthBudgettracker(t)
         

    def printReport(self):
        for budgetAndExpenditure in self.BudgetAndExpenditures:
                # budgetAndExpenditure is a tuple (year, month)
                monthBudgetTracker = self.BudgetAndExpenditures[budgetAndExpenditure]
                totalMonthlyExpenditure = 0
                monthlyIncome=0
                print("For month", monthBudgetTracker.month, "year", monthBudgetTracker.year, "the budget vs expenditure is:")
                for category, expenditure in monthBudgetTracker.BudgetAndExpenditures.items(): 
                    if category == Category.INCOME:
                        monthlyIncome += expenditure
                        continue
                    totalMonthlyExpenditure += expenditure
                    month_budget = self.monthly_budget.get_budget_for(category)
                    print(" For category:", category, "the expenditure is:", expenditure, "and budget is:", month_budget)
                    print(" Remaining budget for the month is:", month_budget + expenditure)    
                print(" your income for the month was " , monthlyIncome ," and total expenditure is: ", totalMonthlyExpenditure )
                print(" your salary account savings are  " , monthlyIncome + totalMonthlyExpenditure)


# Data of Budget Vs Expenditure for user predefined categories for a month
class MonthBudgetTracker:
    def __init__(self, year, month, monthly_budget):
        self.year = year
        self.month = month
        self.monthlyBudget = monthly_budget
        self.BudgetAndExpenditures = {}

    def updateMonthBudgettracker(self , transaction:Transaction) -> bool:
           if self.month == transaction.date.month and self.year == transaction.date.year:
                self.BudgetAndExpenditures[transaction.category] = \
    self.BudgetAndExpenditures.get(transaction.category, 0) + transaction.amount     
                return True
           else:
                return False 
