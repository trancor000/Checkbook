from django.db import models


TYPE_CHOICES = {
    ('deposit', 'deposit'),
    ('withdrawal', 'withdrawal'),
}


PURCHASE_TYPE = {
    ('food', 'food'),
    ('clothes', 'clothes'),
    ('utilities', 'utilities'),
    ('entertainment', 'entertainment'),
    ('gas', 'gas'),
}

ACCOUNT_TYPE = {
    ('checking', 'checking'),
    ('savings', 'savings'),
    ('credit', 'credit'),
}


class transaction(models.Model):
    date = models.DecimalField(max_length=10)
    type = models.CharField(max_length=30, choices=TYPE_CHOICES)
    amount = models.DecimalField(max_digits=10, default="", blank=True)
    description = models.CharField(max_length=30, choices=PURCHASE_TYPE)
    account = models.CharField(max_length=30, choices=ACCOUNT_TYPE)

    objects = models.Manager()

    def __str__(self):
        return self.name
