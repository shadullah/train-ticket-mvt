from django.shortcuts import render
from train.models import BorrowedTicket

# Create your views here.
def dashboard(req):
    bought_ticket = BorrowedTicket.objects.filter(user= req.user)
    return render(req, 'dashboard/dashboard.html',{
        'ticket': bought_ticket
    })