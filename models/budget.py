# Object for monthly budget for all expenditures category.
from models.category import Category

class MonthlyBudget:
    def __init__(self):
        self.budgets = {  
            Category.FLAT: 17500.0 + 1500.0 + 1200.0 + 1000.0, 
            Category.CONVENIENCE: 20000.0,
            Category.INVESTMENT: 70000.0,
            Category.FOOD: 25000.0,
            Category.UNCATEGORIZED: 0.0,
            Category.INCOME: 0.0,
        }
        

    def get_budget_for(self, category: Category) -> float:
        return self.budgets.get(category, 0)
