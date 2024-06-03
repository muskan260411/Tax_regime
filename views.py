from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm , TaxRegimeForm,  CustomUserLoginForm
from .models import TaxRegime


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'tax_regime/register.html', {'form': form, 'error': 'Authentication failed'})
    else:
        form = CustomUserCreationForm()
    return render(request, 'tax_regime/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomUserLoginForm()
    return render(request, 'tax_regime/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request, 'tax_regime/home.html')


@login_required
def suggestion_report(request):
    suggestions = [
        {"date": "18/04/2024", "no": "SUG/24-25/04/2943", "name": "John Doe", "department": "IT", "division": "Services", "subject": "Login Issues", "status": "Registered", "pending_with": "Admin", "decision_date": "18/04/2024"},
    ]
    return render(request, 'tax_regime/suggestion_report.html', {'suggestions': suggestions})



@login_required
def switch_tax_regime(request):
    try:
        tax_regime = TaxRegime.objects.get(user=request.user)
    except TaxRegime.DoesNotExist:
        tax_regime = TaxRegime(user=request.user)
    
    if request.method == 'POST':
        form = TaxRegimeForm(request.POST, instance=tax_regime)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = TaxRegimeForm(instance=tax_regime)
    
    return render(request, 'tax_regime/switch_tax_regime.html', {'form': form})


