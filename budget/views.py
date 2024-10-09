import os

from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.conf import settings
from .models import Transaction
from .forms import UploadFileForm, InsertTransactionForm
from .utils import import_csv, import_pdf


# Transaction.objects.create(
#     date=request.POST["date"],
#     transaction_type=request.POST["transaction_type"],
#     description=request.POST["description"],
#     amount=request.POST["amount"],
# )


def home_page(request):
    transactions = Transaction.objects.order_by("-date")
    return render(request, "budget/home.html", {"transactions": transactions})


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
    import_func = {"csv": import_csv, "pdf": import_pdf}
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file_name = str(request.FILES["file"])
            if not (file_name.endswith(".csv") or file_name.endswith(".pdf")):
                return render(
                    request,
                    "budget/upload.html",
                    {
                        "form": form,
                        "error_message": "File must be either pdf or csv file.",
                    },
                )
            form.save()
            file_path = os.path.join(settings.MEDIA_ROOT, file_name)
            import_func[file_name[-3:]](file_path)
            return redirect("/")
    else:
        form = UploadFileForm()

    return render(request, "budget/upload.html", {"form": form})

