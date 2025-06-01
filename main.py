from models.budget import MonthlyBudget
from services.llm_interpret_transaction_history import TransactionStatementParser


def main():
    income = 165000  # Monthly income TODO take input from user
    budget = MonthlyBudget()

    parser = TransactionStatementParser(r"C:\Users\Sahil Gautam\Desktop\Personal Projects\PersonalBudgetizer\services\raw_statement.csv")
    transactions = parser.parse()
    for t in transactions:
        print(t.date, " ",t.amount," ",t.description," ", t.category)
    #print(transactions)
    # calculator = BudgetCalculator(transactions, budget)
    # #calculator.assign_categories()
    # summary = calculator.summarize()

    # tracker = BudgetTracker(summary, budget)
    # tracker.print_report()

if __name__ == "__main__":
    main()