from django import forms
from expense.models import Transaction, Category

class TransactionForm(forms.ModelForm):
    amount = forms.IntegerField()
    comment = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Transaction
        exclude = ('user',)

class CategoryForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Category
        fields = ('name', )


