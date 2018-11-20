from django import forms

from bootstrap_datepicker_plus import DatePickerInput

from .models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'published_date': DatePickerInput()
        }