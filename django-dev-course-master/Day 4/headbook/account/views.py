from django.shortcuts import render
from .models import Account, Friendship

def all_accs(request):
    accounts = Account.objects.all()
    context = {
        'accounts' : accounts
    }
    return render(request, 'account/all.jinja', context)

def acc(request, id):
    account = Account.objects.get(id = id)
    context = {
        'account' : account,
        'friends': Friendship.objects.get(person = account).friends.all()
    }
    return render(request, 'account/account.jinja', context)