from django.db import models
from datetime import date

# Create your models here.
class Transaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ("IN", "Income"),
        ("EX", "Expense"),
        ("TR", "Transfer"),
    ]
    
    date=models.DateField(default=date.today)
    transaction_type=models.CharField(
        max_length=3,
        choices=TRANSACTION_TYPE_CHOICES,
        default="IN"
    )
    description=models.TextField()
    amount=models.DecimalField(max_digits=10, decimal_places=2)
    created_at=models.DateTimeField(auto_now_add=True)
