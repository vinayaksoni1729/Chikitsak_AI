from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import add_data
from .models import *
from .trial import printdata
def new(request):
    form = add_data(request.POST or None)
    if form.is_valid():
        form.save()
        form = add_data()
        
        return redirect("outputnew")
    dict5 = {"form": form}
    return render(request, "index.html", dict5)
    
def outputnew(request):
    
    command = request.POST['problem']
    from .command import command_output
    varx=command_output(command)
    context = {
      "cmd": varx[0],
      "cmd2":varx[1]
    }
    return render(request, "rindex.html" , context)
