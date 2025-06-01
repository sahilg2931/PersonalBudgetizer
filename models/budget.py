# Models Category of expenditures
from models.category import Category

class MonthlyBudget:
    def __init__(self):
        self.budgets = { # TODO take this values from user 
            Category.FLAT: 17500.0 + 1500.0 + 1200.0 + 1000.0, 
            Category.CONVENIENCE: 30000.0,
            Category.INVESTMENT: 50000.0,
            Category.UNCATEGORIZED: 0.0,
            Category.INCOME: 0.0,
        }
        

    def get_budget_for(self, category: Category) -> float:
        return self.budgets.get(category, 0)
