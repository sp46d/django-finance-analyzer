from django import forms
from django.contrib.admin.options import widgets


class UploadFileForm(forms.Form):
    file = forms.FileField()


class InsertTransactionForm(forms.Form):
    TRANSACTION_TYPE_CHOICES = [
        ("expense", "Expense"),
        ("income", "Income"),
        ("transfer", "Transfer"),
    ]
    
    date = forms.DateField()
    transaction_type = forms.ChoiceField(choices=TRANSACTION_TYPE_CHOICES)
    description = forms.CharField(max_length=200)
    amount = forms.DecimalField(min_value=0, max_digits=10, decimal_places=2)
