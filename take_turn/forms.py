from django import forms
from jalali_date.fields import JalaliDateField,SplitJalaliDateTimeField
from jalali_date.widgets import AdminJalaliDateWidget, AdminSplitJalaliDateTime
from mainpage.models import Take_Turn
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
'''
CHOICE_LIST1 = [
    ('', 'روز هاي هفته'), # replace the value '----' with whatever you want, it won't matter
    (0, 'شنبه'),
    (1,' یک شنبه '),
    (2,' دوشنبه '),
    (3,' سه شنبه '),
    (4,' چهار شنبه '),
    (5,' پنجشنبه '),
    (6,' جمعه ')
]'''
CHOICE_LIST2 = [
    ('', 'جنسيت'), # replace the value '----' with whatever you want, it won't matter
    (0, 'زن'),
    (1, 'مرد')
]
CHOICE_LIST3 = [
    (1, 'نوع درخواست'), # replace the value '----' with whatever you want, it won't matter
(0, 'حضوری'),
 (1, 'تلفنی'),
  (2, 'فکس')
]


class TakeTurnEditForm(forms.ModelForm):

    Patient = forms.CharField(label='شماره ملی')
    mobile = forms.CharField(label='شماره همراه')
    First_name = forms.CharField(label='نام', required=False)
    Last_name = forms.CharField(label='نام خانوادگی', required=False)
 #   Day= forms.ChoiceField(choices=CHOICE_LIST1, required=False)
    TypeTurn= forms.ChoiceField(choices=CHOICE_LIST3, required=False)
    class Meta:
        model = Take_Turn
        fields = (
         'part',
         'date_time','Description')
    def __init__(self, *args, **kwargs):
        super(TakeTurnEditForm,self).__init__(*args, **kwargs)
        self.fields['Patient'].widget.attrs['class'] = 'form-control'
        self.fields['mobile'].widget.attrs['class'] = 'form-control'
        self.fields['First_name'].widget.attrs['class'] = 'form-control'
        self.fields['Last_name'].widget.attrs['class'] = 'form-control'
        self.fields['TypeTurn'].widget.attrs['class'] = 'form-control'
        self.fields['part'].widget.attrs['class'] = 'form-control'
        self.fields['date_time'].widget.attrs['class'] = 'form-control'
        self.fields['Description'].widget.attrs['class'] = 'form-control'
        self.fields['date_time'] = SplitJalaliDateTimeField(label=('date time'),)
class TakeTurnEditForm_S(forms.ModelForm):
 #   Day= forms.ChoiceField(choices=CHOICE_LIST1, required=False)
    TypeTurn= forms.ChoiceField(choices=CHOICE_LIST3, required=False)
    class Meta:
        model = Take_Turn
        fields = (
         'part','date_time',
          'Description')
    def __init__(self, *args, **kwargs):
        super(TakeTurnEditForm_S,self).__init__(*args, **kwargs)
        self.fields['TypeTurn'].widget.attrs['class'] = 'form-control'
        self.fields['part'].widget.attrs['class'] = 'form-control'
        self.fields['date_time'].widget.attrs['class'] = 'form-control'
        self.fields['Description'].widget.attrs['class'] = 'form-control'


        self.fields['date_time'] = SplitJalaliDateTimeField(label=('date time'),)
        self.fields['date_time'].empty_label='--كلينيك--'
