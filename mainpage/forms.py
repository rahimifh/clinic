from django import forms
from .models import Patient,day_of
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
class Searchbox (forms.Form):
    searchtxt=forms.CharField (max_length=100, widget=forms.TextInput(attrs={'class':'search-input', 'placeholder':"جستجوی پرونده" }))
class patientEditForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('NationalCode', 'p_name', 'last_name', 'mobile','land_line_phone','age','Gender')
    def __init__(self, *args, **kwargs):
        super(patientEditForm,self).__init__(*args, **kwargs)
        self.fields['NationalCode'].widget.attrs['class'] = 'form-control'
        self.fields['p_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['mobile'].widget.attrs['class'] = 'form-control'
        self.fields['land_line_phone'].widget.attrs['class'] = 'form-control'
        self.fields['age'].widget.attrs['class'] = 'form-control'
        self.fields['Gender'].widget.attrs['class'] = 'form-control'
CHOICE_LIST = [
    ('', 'جنسیت'), # replace the value '----' with whatever you want, it won't matter
    (0, 'زن'),
    (1, 'مرد')
]
class patientTotalForm(forms.ModelForm):
    Gender=forms.ChoiceField(choices=CHOICE_LIST, required=False)
    class Meta:
        model = Patient
        fields = ( 'NationalCode','p_name', 'last_name', 'mobile','land_line_phone','age')
    def __init__(self, *args, **kwargs):
        super(patientTotalForm,self).__init__(*args, **kwargs)
        self.fields['Gender'].empty_label = "(Select here)"
        self.fields['Gender'].widget.attrs['class'] = 'siavash'

class day_ofEditForm(forms.ModelForm):
    class Meta:
        model = day_of
        fields = ('date_time','Description')
    def __init__(self, *args, **kwargs):
        super(day_ofEditForm,self).__init__(*args, **kwargs)
        self.fields['date_time'] = JalaliDateField(label=('تاریخ'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget
           # optional, to use default datepicker
        )
        self.fields['date_time'].widget.attrs['class'] = 'form-control'
        self.fields['Description'].widget.attrs['class'] = 'form-control'
class Filter_form(forms.Form):
    from_date = forms.DateTimeField()
    to_date = forms.DateTimeField()
    def __init__(self, *args, **kwargs):
        super(Filter_form,self).__init__(*args, **kwargs)
        self.fields['from_date'] = JalaliDateField(label=('از تاریخ'), # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget
           # optional, to use default datepicker
        )
        self.fields['to_date'] = JalaliDateField(label=("تا تاریخ"),  # date format is  "yyyy-mm-dd"
            widget=AdminJalaliDateWidget
           # optional, to use default datepicker
        )
