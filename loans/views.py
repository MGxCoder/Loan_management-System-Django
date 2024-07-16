from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Application
from .forms import ApplicationForm

def home(request):
    return redirect('login')

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect('customer_dashboard')
    applications = Application.objects.all()
    return render(request, 'loans/admin_dashboard.html', {'applications': applications})

@login_required
def customer_dashboard(request):
    applications = Application.objects.filter(user=request.user)
    return render(request, 'loans/customer_dashboard.html', {'applications': applications})

@login_required
def apply_loan(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            return redirect('customer_dashboard')
    else:
        form = ApplicationForm()
    return render(request, 'loans/apply_loan.html', {'form': form})
