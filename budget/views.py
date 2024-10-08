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
    transactions = Transaction.objects.order_by("-date")
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


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES["file"]
            import_csv(file)
            return redirect("/")
    else:
        form = UploadFileForm()
        
    return render(request, "budget/upload.html", {"form": form})
            
        
    # else:
        # form = UploadFileForm()
    return HttpResponse("No files have been uploaded.")

