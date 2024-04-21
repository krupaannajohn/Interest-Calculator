"""from django.shortcuts import render,redirect
from .forms import calculationForm
from .models import Calculation

# Create your views here: each view is associated with a template, here we do all the functions and operations that are to be done in the backend
def index(request):
    if request.method=='POST':   #post method is used when the user posts something to the server or clicks a button etc.
        form=calculationForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.result=instance.principal*(instance.rate/100)*instance.time
            instance.save()
            return redirect('index')
        
    else:
        form=calculationForm()      # if user doesnt send/post any request. then itll just load the form automatically
    calculations=Calculation.objects.all().order_by('-timestamp')    # calculation is our mode, objects refers to the entire data from this particular model and it allows to order according to the timestamp
    return render(request,'index.html',{'form':form,'calculations':calculations})"""

from django.shortcuts import render, redirect, get_object_or_404
from .forms import calculationForm
from .models import Calculation

# Create your views here: each view is associated with a template, here we do all the functions and operations that are to be done in the backend
def index(request):
    if request.method == 'POST':   # post method is used when the user posts something to the server or clicks a button etc.
        form = CalculationForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.result = instance.principal * (instance.rate / 100) * instance.time
            instance.save()
            return redirect('index')
    else:
        form = CalculationForm()  # if user doesn't send/post any request. then it'll just load the form automatically
    calculations = Calculation.objects.all().order_by('-timestamp')  # calculation is our mode, objects refers to the entire data from this particular model and it allows to order according to the timestamp
    return render(request, 'index.html', {'form': form, 'calculations': calculations})

def delete_calculation(request, calculation_id):
    calculation = get_object_or_404(Calculation, pk=calculation_id)
    calculation.delete()
    return redirect('index')
