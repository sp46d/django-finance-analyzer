from django.shortcuts import render, redirect
from .models import Transaction


def home(request):
    if request.method == "POST":
        Transaction.objects.create(
            date=request.POST["date"],
            transaction_type=request.POST["transaction_type"],
            description=request.POST["description"],
            amount=request.POST["amount"],
        )
        return redirect("/")

    transactions = Transaction.objects.order_by("-created_at").all()
    return render(request, "budget/home.html", {"transactions": transactions})
