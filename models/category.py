from enum import Enum

class Category(str, Enum):
    FLAT = "FlatExpenditures"
    CONVENIENCE = "ConvenienceExpenditures"
    FOOD = "FoodExpenditures"
    INVESTMENT = "Investment"
    UNCATEGORIZED = "UncategorizedExpenditures"
    INCOME = "Income"

    @classmethod
    def list(cls):
        return [cls.FLAT, cls.CONVENIENCE, cls.FOOD, cls.INVESTMENT, cls.UNCATEGORIZED, cls.INCOME]
