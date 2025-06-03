from models.budget import MonthlyBudget
from services.llm_interpret_bank_statement import TransactionStatementParser
from services.tracker import BudgetTracker
from models.category import Category
import services.summary_llm_transaction_category as  summary_llm_transaction_category 

def main():
    monthlyIncome = 0  # Monthly income TODO take input from user
    budget = MonthlyBudget() # TODO take these values from user

    parser = TransactionStatementParser(r"C:\Users\Sahil Gautam\Desktop\Personal Projects\PersonalBudgetizer\services\raw_transaction.csv.csv")
    # list of Transaction objects (date , amount , description , category) 
    # interpreted using ai from bank statements
    transactions = parser.parse()
    
    tracker = BudgetTracker(budget)
    tracker.updateBudgetTracker(transactions)   
    
    summaryUncategorized = summary_llm_transaction_category.getSummaryForTransactionCategory(transactions, Category.UNCATEGORIZED, budget)
    print(summaryUncategorized)

if __name__ == "__main__":
    main()