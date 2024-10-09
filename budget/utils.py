import csv
import re
import pdftotext
from pathlib import Path
from .models import Transaction
from datetime import datetime


def import_csv(file_path: Path) -> None:
    with open(file_path, "r") as f:
        reader = csv.DictReader(f)
        for line in reader:
            Transaction.objects.create(**line)


def import_pdf(file_path: Path) -> None:
    parsed_transactions = read_pdf_statement(file_path)
    for transaction in parsed_transactions:
        date = datetime.strptime(transaction["date"], "%m/%d/%y")
        transaction["date"] = date.strftime("%Y-%m-%d")
        amount = transaction["amount"].replace(",", "")
        if amount.startswith("-"):
            transaction["transaction_type"] = "expense"
            transaction["amount"] = amount[1:]
        else:
            transaction["transaction_type"] = "income"
            transaction["amount"] = amount
        Transaction.objects.create(**transaction)
    

def read_pdf_statement(file_path: Path) -> list[dict[str, str]]:
    TRANSACTION_PATTERN = (
        r"(?P<date>\d+/\d+/\d+) +"
        r"(?P<description>.*?)\s*"
        r"(?P<amount>[-\d.,]+)$"   
    )
    transactions = []
    with open(file_path, "rb") as f:
        pdf = pdftotext.PDF(f, physical=True)
        for page in pdf:
            for line in page.splitlines():
                match = re.match(TRANSACTION_PATTERN, line)
                if match:
                    transactions.append(match.groupdict())
    
    return transactions