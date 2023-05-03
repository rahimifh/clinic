from django import forms
from jalali_date.fields import JalaliDateField,SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from .models import PaymentReceipt,refer_to_surgery
from mainpage.models import Reception
class paymentEditForm(forms.Form):
    price = forms.CharField(label='ثبت مبلغ جدید')
    state = forms.CharField(widget=forms.HiddenInput(), initial="1")
    def __init__(self, *args, **kwargs):
        super(paymentEditForm,self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['class'] = 'form-control'

class ReceptionEditForm(forms.ModelForm):
    services = forms.CharField(label='خدمات گرفته شد')
    # diagnisis = forms.CharField(label='تشخیص ها')
    class Meta:
        model = Reception
        fields = ('TurnCode',
         'date','Referrer','Description')
    def __init__(self, *args, **kwargs):
        super(ReceptionEditForm,self).__init__(*args, **kwargs)
        self.fields['date'] = SplitJalaliDateTimeField(label=('تاریخ نوبت'),
                     # required, for decompress DatetimeField to JalaliDateField and JalaliTimeField
                )
        self.fields['Referrer'].required = False
        self.fields['services'].widget.attrs['class'] = 'form-control'
        # self.fields['diagnisis'].widget.attrs['class'] = 'form-control'
        self.fields['TurnCode'].widget.attrs['class'] = 'form-control'
        self.fields['date'].widget.attrs['class'] = 'form-control'
        self.fields['Referrer'].widget.attrs['class'] = 'form-control'
        self.fields['Description'].widget.attrs['class'] = 'form-control'

class surgeryEditForm(forms.ModelForm):
    class Meta:
        model = refer_to_surgery
        fields = ('name','name_Doc','date_time','patient_history','Medical_innocence')
    def __init__(self, *args, **kwargs):
        super(surgeryEditForm,self).__init__(*args, **kwargs)

        self.fields['date_time'] = JalaliDateField(label=('تاريخ جراحي'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name_Doc'].widget.attrs['class'] = 'form-control'
        self.fields['date_time'].widget.attrs['class'] = 'form-control'
        self.fields['patient_history'].widget.attrs['class'] = 'form-control'
        self.fields['Medical_innocence'].widget.attrs['class'] = 'form-control'
class refToSurgeryEditForm(forms.ModelForm):
    NationalCode = forms.CharField(label='کد ملی')
    class Meta:
        model = refer_to_surgery
        fields = ('name','name_Doc','date_time','patient_history','Medical_innocence')
    def __init__(self, *args, **kwargs):
        super(refToSurgeryEditForm,self).__init__(*args, **kwargs)
        self.fields['NationalCode'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name_Doc'].widget.attrs['class'] = 'form-control'
        self.fields['date_time'].widget.attrs['class'] = 'form-control'
        self.fields['patient_history'].widget.attrs['class'] = 'form-control'
        self.fields['Medical_innocence'].widget.attrs['class'] = 'form-control'
        self.fields['date_time'] = JalaliDateField(label=('تاريخ جراحي'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget # optional, to use default datepicker
        )


class PayReceiptEditForm(forms.ModelForm):
    state = forms.CharField(widget=forms.HiddenInput(), initial="2")
    class Meta:
        model = PaymentReceipt
        fields = ('Device', 'mobile', 'Paid')
    def __init__(self, *args, **kwargs):
        super(PayReceiptEditForm,self).__init__(*args, **kwargs)
        self.fields['Device'].widget.attrs['class'] = 'form-control'
        self.fields['mobile'].widget.attrs['class'] = 'form-control'
        self.fields['Paid'].widget.attrs['class'] = 'form-control'
