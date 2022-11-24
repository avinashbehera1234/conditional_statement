from django.shortcuts import render

# Create your views here.
def condition(request):
    d={'a':150,'b':330,'c':400}
    return render(request,'condition.html',context=d)
