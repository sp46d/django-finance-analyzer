import csv
from .models import Transaction


def import_csv(file) -> None:
    csv_data = file.read().decode("utf-8").splitlines()
    reader = csv.DictReader(csv_data)
    for line in reader:
        Transaction.objects.create(**line)
