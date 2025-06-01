from models.category import Category
import datetime

class Transaction:
    def __init__(self, date : datetime.date, amount: float, description: str, category: Category = Category.UNCATEGORIZED):
        self.date = date
        self.amount = amount
        self.description = description
        self.category = category

    def assign_category(self, category: Category):
        self.category = category
