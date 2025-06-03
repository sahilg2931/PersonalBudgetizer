# Uses cohere model to interpret messy bank statements to convert them into clean csv
# and then convert the transactions into Transaction object

import io
from typing import Optional
from datetime import datetime
import csv
from models.transaction import Transaction
from models.category import Category
import services.llm_prompt_response as llm_prompt_response


class TransactionStatementParser:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def parse(self):
        transactions = []
        raw_text = read_statement_csv(self.file_path)
        clean_csv_result = extract_transactions_with_llm(raw_text) 
        csv_file_like = io.StringIO(clean_csv_result.strip())
        reader = csv.DictReader(csv_file_like)
        for row in reader:
            try:
                date_str = row['date']  # e.g. '02/06/2025'
                date_obj = datetime.strptime(date_str, '%d/%m/%Y').date()
                amount = float(row['amount'])
                description = row['description']
                category_str = row['category']
                category_enum = Category(category_str)
                transactions.append(Transaction(date_obj,amount, description, category_enum))
            except (ValueError, KeyError) as e:
                print(f"Skipping invalid row: {row} — Error: {e}")
        return transactions

PREDEFINED_CATEGORIES = [
    "FlatExpenditures",          # Rent, maid, electricity, maintenance
    "ConvenienceExpenditures",   # Clothes, gadgets, shopping, hygiene, fuel, cabs
    "FoodExpenditures",                      # All food and deliveries
    "Investment",                # Monthly investments
    "UncategorizedExpenditures",          # Uncategorized/others
    "Income"            # credit from either refunds or salary or any money that comes into account
]

def read_statement_csv(file_path: str) -> str:
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = [", ".join(row) for row in reader]
    return "\n".join(rows)


def extract_transactions_with_llm(statement_text: str) -> str:
    prompt = f"""
You are a helpful assistant that converts messy Indian bank statements into a clean and categorized CSV.

From the following raw bank statement text, extract only the transactions into a CSV format with these four columns:
- date (format: DD/MM/YYYY)
- description (keep it same as is)
- amount (positive if credited, negative if debited)
- category (must be one of these: {", ".join(PREDEFINED_CATEGORIES)})

Categorize based on the description. Use:
- FlatExpenditures for rent, maid, electricity, flat maintenance
- ConvenienceExpenditures for shopping, hygiene, gadgets, fuel, cabs
- FoodExpenditures for any food-related purchases or delivery services like Swiggy/Zomato
- Investment for any investment-type deposits
- UncategorizedExpenditures if it doesn't clearly belong to the above
- Income for any salary/income deposits or credit into account

IMPORTANT:
- Return ONLY the CSV content with a header row.
- Do NOT include any markdown code fences (```), extra commentary, or other formatting.
- Make sure the output is exactly a valid CSV.

Here is the raw input:
---
{statement_text}
---
Return the CSV only, no extra comments.
"""
    return llm_prompt_response.call_cohere_chat_with_retry(prompt)


