from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="accounts:login")
def purchase_start_view(request):
    pass


def purchase_success_view():
    pass


def purchase_stopped_view():
    pass
