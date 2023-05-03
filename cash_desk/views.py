from django.shortcuts import render
from .forms import PayReceiptEditForm
from .models import PaymentReceipt
# Create your views here.
def cash_desk_form(request):
    form = PayReceiptEditForm()
    return render(request, "cash_desk/cash_desk.html",{'form':form})
