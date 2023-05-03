from django import forms

from .models import PaymentReceipt
class PayReceiptEditForm(forms.ModelForm):
    class Meta:
        model = PaymentReceipt
        fields = ('EntranceCode', 'p_name', 'last_name', 'age', 'NationalCode','Device', 'Receptionist', 'mobile', 'Payable','Payment')
