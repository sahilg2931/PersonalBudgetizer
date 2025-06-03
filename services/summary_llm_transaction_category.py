import services.llm_prompt_response as llm_prompt_response


def getSummaryForTransactionCategory(transactions, category, monthlyBudget ):
    transactionsCategory = list(filter(lambda transaction: transaction.category == category, transactions))
    prompt = ""
    for transaction in transactionsCategory:
        prompt += f"{transaction.date} {transaction.amount} {transaction.description} {transaction.category}\n"
    return extract_transactions_with_llm(prompt, monthlyBudget.get_budget_for(category))    

def extract_transactions_with_llm(statement_text: str , categoryMonthlyBudget ) -> str:
    prompt = f"""
    You are a financial assistant. You are precise, very good with numbers , accurate , immaculate and insightful  
    Given a list of raw bank transactions with UPI details, description, dates, amounts, and recipients, categorize each transaction and provide a concise summary. 

    Each line is in this format:
    <DATE> <AMOUNT> <TRANSACTION DETAILS> Category

    The category will be same for each of the transactions.
    The total budget for the category is {categoryMonthlyBudget}
     
    Your tasks:
    1. Identify the likely category for each transaction (e.g., Food, Health, Rent, Education, Games, Friends/Transfers, Shopping, Groceries, Bills, etc.).
    2. Group and total the expenses and incomes by category.
    3. Size amount spent with budget.
    4. Provide a clean summary like:
    
    ---
    Summary:
    - Total Spent: ₹xx,xxx
    - Total Received: ₹x,xxx

    Category Breakdown:
    - Food: ₹x,xxx
    - Health: ₹x,xxx
    - Transfers: ₹x,xxx
    - Games: ₹x,xxx
    - ...

    Transactions to flag (unclear category or large amount):
    - <DATE> <AMOUNT> <DETAILS>
    ---

    Here is the transaction list:
    {statement_text}
    """
    return llm_prompt_response.call_cohere_chat_with_retry(prompt)    