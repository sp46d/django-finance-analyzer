from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from .models import Transaction
from .forms import UploadFileForm, InsertTransactionForm
from .utils import import_csv


# Transaction.objects.create(
#     date=request.POST["date"],
#     transaction_type=request.POST["transaction_type"],
#     description=request.POST["description"],
#     amount=request.POST["amount"],
# )


def home_page(request):
    transactions = Transaction.objects.all()
    return render(
        request, "budget/home.html", {"transactions": transactions}
    )

def new_transaction(request):
    if request.method == "POST":
        form = InsertTransactionForm(request.POST)
        if form.is_valid():
            Transaction.objects.create(**form.cleaned_data)
            return redirect("/")
    else:
        form = InsertTransactionForm()
        
    return render(request, "budget/typing.html", {"form": form})
# def upload_file(request):

#     # file = request.FILES["file"]
#     # import_csv(file)
#     return HttpResponse(f"{str(file)} imported successfully.")
