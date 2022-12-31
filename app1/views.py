from django.shortcuts import render

# Create your views here.
def operation(request):
    d={'a':66123,'b':225,'c':2388}
    return render(request,'operation.html',d)
