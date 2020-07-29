from django.shortcuts import render
from django.http import HttpResponse
from tablib import Dataset

# Create your views here.
def dashboard_home(request):
    return HttpResponse("<h1>dashboard home</h1>")

def dashboard_estudiante(request):
    return HttpResponse("<h1>dashboard estudiante</h1>")

def importar(request):
    if request.method == 'POST':
       tablonejercicios_resource = tablonejercicios_resource()
       dataset = Dataset()
       nuevo_tablon=request.FILES['csvfile']
       imported_data=dataset.load(nuevo_tablon.read())
       result = tablonejercicios_resource.import_data(dataset,dry_run=True)
       if not result.has_errors():
           tablonejercicios_resource.import_data(dataset,dry_run=False)
    return render(request,'export/importar.html')