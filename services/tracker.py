from models.category import Category

class BudgetTracker:
    def __init__(self, categorized_data, monthly_budget):
        self.categorized_data = categorized_data
        self.monthly_budget = monthly_budget

    def print_report(self):
        print("=== Budget Report ===")
        for category in Category.list():
            allocated = self.monthly_budget.get_budget_for(category)
            spent = self.categorized_data.get(category, 0)
            status = "✅ Within Budget" if spent <= allocated else "⚠️ Over Budget"
            print(f"{category.value}: Allocated ₹{allocated}, Spent ₹{spent} → {status}")
