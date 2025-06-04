import services.llm_prompt_response as llm_prompt_response
from collections import defaultdict

def getSummaryForTransactionCategoryMonthly(transactions, category, monthlyBudget):
    transactionsCategory = list(filter(lambda transaction: transaction.category == category, transactions))

    # Group transactions by (year, month)
    grouped_by_month = defaultdict(list)
    for transaction in transactionsCategory:
        month_key = (transaction.date.year, transaction.date.month)
        grouped_by_month[month_key].append(transaction)

    # Aggregate summaries per month
    summaries = []
    for (year, month), month_transactions in sorted(grouped_by_month.items()):
        summary = get_summary_for_category_month(month_transactions, category, monthlyBudget, year, month)
        summaries.append(summary)

    return "\n\n".join(summaries)


def get_summary_for_category_month(transactions, category, monthlyBudget, year, month):
    prompt = ""
    for transaction in transactions:
        prompt += f"{transaction.date} {transaction.amount} {transaction.description} {transaction.category}\n"

    category_budget = monthlyBudget.get_budget_for(category)
    month_summary = extract_transactions_with_llm(prompt, category_budget)

    # Add month header
    header = f"\n=== Summary for {month:02d}/{year} ===\n"
    return header + month_summary.strip()


def extract_transactions_with_llm(statement_text: str, categoryMonthlyBudget) -> str:
    prompt = f"""
You are a financial assistant. You are precise, very good with numbers, accurate, immaculate and insightful.

Given a list of raw bank transactions with UPI details, description, dates, amounts, and recipients, categorize each transaction and provide a concise summary. 

Each line is in this format:
<DATE> <AMOUNT> <TRANSACTION DETAILS> Category

The category will be the same for all the transactions.
The total monthly budget for this category is ₹{categoryMonthlyBudget}.

Your tasks:
1. Identify the likely category for each transaction (e.g., Food, Health, Rent, Education, Games, Friends/Transfers, Shopping, Groceries, Bills, etc.).
2. Group and total the expenses and incomes by category.
3. Compare total spending to the budget.
4. Provide a clean summary like:

---
Summary:
- Total Spent: ₹xx,xxx
- Total Received: ₹x,xxx

Category Breakdown:
- Food: ₹x,xxx
- Transfers: ₹x,xxx
...

Transactions to flag (unclear category or large amount):
- <DATE> <AMOUNT> <DETAILS>
---

Here is the transaction list:
{statement_text}
"""
    return llm_prompt_response.call_cohere_chat_with_retry(prompt, 8000)
