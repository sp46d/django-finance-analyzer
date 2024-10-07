import csv
from .models import Transaction
# import os
# from pathlib import Path

# BASE_DIR = Path(".").resolve()
# file = os.path.join(BASE_DIR, "artificial_data", "test.csv")


def import_csv(file) -> None:
    csv_data = file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(csv_data)
    for line in reader:
        Transaction.objects.create(**line)
