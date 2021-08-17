from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import TransactionForm
from .models import transaction



def admin_console(request):
    transactions = transaction.objects.all()
    return render(request, 'account/transactions_page.html', {'accounts': accounts})


def details(request, pk):
    pk = int(pk)
    item = get_object_or_404(transaction, pk=pk)
    form = transaction(data=request.POST or None, instance=item)
    if request.method == 'POST':
        if form.is_valid():
            form2 = form.save(commit=False)
            form2.save()
            return redirect('admin_console')
        else:
            print(form.errors)
    else:
        return render(request, 'accounts/transactions_product.html', {'form': form})


def delete(request, pk):
    pk = int(pk)
    item = get_object_or_404(transaction, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('admin_console')
    context = {"item": item, }
    return render(request, "account/confirmDelete.html", context)


def confirmed(request):
    if request.method == 'POST':
        # creates form instance and binds data to it
        form = transaction(request.POST or None)
        if form.is_valid():
            form.delete()
            return redirect('admin_console')
    else:
        return redirect('admin_console')


def createRecord(request):
    form = TransactionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('admin_console')
    else:
        print(form.errors)
        form = TransactionForm()
    context = {
        'form': form,
    }
    return render(request, 'account/createRecord.html', context)
