from collections import defaultdict
from models.category import Category
from services.llm_classifier import classify_transaction_llm

class BudgetCalculator:
    def __init__(self, transactions, monthly_budget):
        self.transactions = transactions
        self.monthly_budget = monthly_budget
        self.categorized = defaultdict(float)

    def assign_categories(self):
        for transaction in self.transactions:
            if transaction.category is None:
                predicted_category_str = classify_transaction_llm(transaction.description)
                predicted_category = Category(predicted_category_str)
                transaction.assign_category(predicted_category)

    def summarize(self):
        for transaction in self.transactions:
            self.categorized[transaction.category] += transaction.amount
        return self.categorized
