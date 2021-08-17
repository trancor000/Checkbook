from django.forms import ModelForm
from .models import transaction


class TransactionForm(ModelForm):
    class Meta:
        model = transaction
        fields = '__all__'

