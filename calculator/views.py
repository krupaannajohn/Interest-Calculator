from django.shortcuts import render, redirect, get_object_or_404
from .forms import calculationForm
from .models import Calculation

def index(request):
    if request.method == 'POST':   
        form = calculationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.result = instance.principal * (instance.rate / 100) * instance.time
            instance.save()
            return redirect('index')
    else:
        form = calculationForm()  
    calculations = Calculation.objects.all().order_by('-timestamp')  
    return render(request, 'index.html', {'form': form, 'calculations': calculations})

def delete_calculation(request, calculation_id):
    calculation = get_object_or_404(Calculation, pk=calculation_id)
    calculation.delete()
    return redirect('index')
