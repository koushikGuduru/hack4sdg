from django.shortcuts import render

# Create your views here.


from django.shortcuts import render, redirect
from .forms import DonationForm
from .models import Donation

def donate(request):
    if request.method == 'POST':
        form = DonationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('donations:thanks')
    else:
        form = DonationForm()
    return render(request, 'donations/donate.html', {'form': form})

def thanks(request):
    return render(request, 'donations/thanks.html')